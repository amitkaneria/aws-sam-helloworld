import requests
import datetime
# from datetime import datetime
import time
from datetime import date
from finance.project_gamma.alphavantage.dao.dao import insert_daily_price_volume, update_daily_price_volume, update_daily_technicals_stochs, update_daily_technicals_ema, update_daily_technicals_rsi, get_status    \
    ,insert_monthly_fundamentals
from finance.project_gamma.alphavantage.util.util import is_valid_date
from finance.project_gamma.alphavantage.util.util import last_business_day, previous_business_day, next_business_day, \
    next_week_business_day, friday_before_previous_friday, previous_friday
from finance.project_gamma.alphavantage.dao.dao import update_status, get_tickers, insert_monthly_fundamentals
from finance.project_gamma.alphavantage.dao.data_analytics_dao import process_signals
from dotenv import load_dotenv
import os
load_dotenv()

DAILY_DATA_COLLECTION_START_DATE = os.environ.get('WEEKLY_DATA_COLLECTION_START_DATE')
WEEKLY_DATA_COLLECTION_START_DATE = os.environ.get('WEEKLY_DATA_COLLECTION_START_DATE')
API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')


def process_fundamentals_monthly_for(priority):
    ticker_list_db = get_tickers(interval='monthly', last_run_date=None, priority=priority)
    print("##### Running MONTHLY for Date: "+ datetime.datetime.now().strftime("%Y-%m-%d") + " for List: " str(ticker_list_db))
    counter=0
    for ticker in ticker_list_db:
        counter = counter + 1
        print("## Running Ticker: " + ticker )
        process_fundamentals_for(ticker=ticker, api_key=API_KEY)
        update_status(ticker, interval='monthly', date=datetime.datetime.now().strftime("%Y-%m-%d"))
        if counter%5 == 0:
            print(str(datetime.datetime.now()) + ' : . . . sleeping')
            time.sleep(50)


def process_daily_priority_for(priority):
    process_priority_for(interval='daily', priority=priority)


def process_weekly_priority_for(priority):
    process_priority_for(interval='weekly', priority=priority)


def process_priority_for(interval, priority):
    global ticker_list_db, ticker
    ticker_list_db = get_tickers(interval=interval, last_run_date=None, priority=priority)
    print(f"Priority: {priority}, Running {interval} for List:" + str(ticker_list_db))
    for ticker in ticker_list_db:
        print(str(datetime.datetime.now()) + ' : ##### ##### ' + ticker + ' ##### #####')
        # process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-07-16')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        process_data_for(ticker, api_key=API_KEY, interval=interval, date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(30)
    if len(ticker_list_db) > 0:
        # Daily Analytics Run
        generate_signal(interval='daily', start_date=str(previous_business_day(last_business_day(None))), end_date=None)
    else:
        print('NOTE: Analytics is not NOT for empty watch-list')
    print('##### ##### ##### ##### #####')


def process_data_for(ticker, api_key, interval, date):


    ## Pricing Data
    if interval == 'daily' or interval == 'weekly':
        try:
            process_price_volume_data_for(ticker, api_key, interval=interval, date=date)
        except requests.exceptions.ConnectionError:
            time.sleep(60)
            process_price_volume_data_for(ticker, api_key, interval=interval, date=date)
    elif interval == '60min':
        try:
            process_intraday_price_volume_data_for(ticker, api_key, interval=interval, date=date)
        except requests.exceptions.ConnectionError:
            time.sleep(60)
            process_intraday_price_volume_data_for(ticker, api_key, interval=interval, date=date)


    ## Stochastic Daya
    try:
        process_stochastic_data_for(ticker, api_key, interval=interval, date=date)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        process_stochastic_data_for(ticker, api_key, interval=interval, date=date)


    ## EMA-8 Data
    try:
        process_ema8_data_for(ticker, api_key, interval=interval, date=date)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        process_ema8_data_for(ticker, api_key, interval=interval, date=date)


    ## EMA-12 Data
    try:
        process_ema12_data_for(ticker, api_key, interval=interval, date=date)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        process_ema12_data_for(ticker, api_key, interval=interval, date=date)


    print(str(datetime.datetime.now()) + ' : . . . sleeping')
    time.sleep(25)


    ## EMA-21 Data
    try:
        process_ema21_data_for(ticker, api_key, interval=interval, date=date)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        process_ema21_data_for(ticker, api_key, interval=interval, date=date)


    ## EMA-50 Data
    if interval == 'daily':
        try:
            process_ema50_data_for(ticker, api_key, interval=interval, date=date)
        except requests.exceptions.ConnectionError:
            time.sleep(60)
            process_ema50_data_for(ticker, api_key, interval=interval, date=date)


    ## EMA-200 Data
    if interval == 'daily':
        try:
            process_ema200_data_for(ticker, api_key, interval=interval, date=date)
        except requests.exceptions.ConnectionError:
            time.sleep(60)
            process_ema200_data_for(ticker, api_key, interval=interval, date=date)


    ## RSI Data
    try:
        process_rsi_data_for(ticker, api_key, interval=interval, date=date)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        process_rsi_data_for(ticker, api_key, interval=interval, date=date)


    ###### Update DB Status
    # insert_status(ticker, interval=interval, date=datetime.datetime.now().strftime("%Y-%m-%d"))
    update_status(ticker, interval=interval, date=datetime.datetime.now().strftime("%Y-%m-%d"))


def generate_signal(interval='daily', start_date='2020-12-31', end_date=None):


    if end_date == None:
        end_date = datetime.date.today()
    else:
        end_date = datetime.datetime.strptime(str(end_date), '%Y-%m-%d').date()


    if interval == 'daily':
        next_business_date = next_business_day(start_date)
    elif interval == 'weekly':
        next_business_date = next_week_business_day(start_date)


    print("##### Generating Report for Interval :" + interval)
    while next_business_date <= datetime.date.today() and next_business_date <= end_date:

        print("##### START DATE : " + str(start_date) + " , ## END DATE : " + str(next_business_date))

        ## Potential trend change indicators
        process_signals(start_date, end_date=next_business_date, interval=interval, method='stoch.slow', buy_sell='buy')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='stoch.slow', buy_sell='sell')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='rsi', buy_sell='buy')
        # process_signals(start_date, end_date=next_business_date, interval=interval, method='rsi', buy_sell='sell')

        ## Strong trend indicators
        process_signals(start_date, end_date=next_business_date, interval=interval, method='ema.8.12', buy_sell='buy')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='ema.8.12', buy_sell='sell')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='ema.21', buy_sell='buy')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='ema.21', buy_sell='sell')

        ## Special Indicators
        # process_signals(start_date, end_date=next_business_date, interval=interval, method='amit.special', buy_sell='buy')
        # process_signals(start_date, end_date=next_business_date, interval=interval, method='amit.special', buy_sell='sell')

        start_date = next_business_date
        if interval == 'daily':
            next_business_date = next_business_day(start_date)
        elif interval == 'weekly':
            next_business_date = next_week_business_day(start_date)


def process_price_volume_data_for(ticker, api_key, interval, date):


    if interval == 'daily':
        interval_enum = 'TIME_SERIES_DAILY'
    elif interval == 'weekly':
        interval_enum = 'TIME_SERIES_WEEKLY'

    url = 'https://www.alphavantage.co/query?function={0}&symbol={1}&outputsize=full&apikey={2}'.format(interval_enum, ticker, api_key)

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        r = requests.get(url)

    response_data = r.json()
    if interval == 'daily':
        data = response_data['Time Series (Daily)']
    elif interval == 'weekly':
        data = response_data['Weekly Time Series']

    print(str(datetime.datetime.now()) + ' : . Price/Volume data')
    if is_valid_date(date):
        try:
            try:
                insert_daily_price_volume(ticker, date, interval, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            except:
                new_date = date+" 16:00:01"
                insert_daily_price_volume(ticker, new_date, interval, data[new_date]['1. open'], data[new_date]['2. high'], data[new_date]['3. low'], data[new_date]['4. close'], data[new_date]['5. volume'])
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Price/Volume data(" + url + ") NOT FOUND!!!... Moving to the next one!!!")

    else:
        last_run = get_status(ticker, interval=interval)
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            if interval == 'daily':
                start_date = datetime.datetime.strptime(DAILY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()
            elif interval == 'weekly':
                start_date = datetime.datetime.strptime(WEEKLY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()

            if last_run == None:
                last_run = start_date

            if new_date > start_date and new_date > last_run:
                insert_daily_price_volume(ticker, date, interval, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            else:
                break

def process_intraday_price_volume_data_for(ticker, api_key, interval, date):

    if interval == '60min':
        interval_enum = 'TIME_SERIES_INTRADAY'

    if interval == '60min':
        url = 'https://www.alphavantage.co/query?function={0}&symbol={1}&interval={2}&apikey={3}'.format(interval_enum, ticker, time_period, api_key)

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        r = requests.get(url)

    response_data = r.json()
    if interval == '60min':
        data = response_data['Time Series (60min)']

    print(str(datetime.datetime.now()) + ' : . Price/Volume data')
    if is_valid_date(date):
        try:
            try:
                insert_daily_price_volume(ticker, date, interval, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            except:
                new_date = date+" 16:00:01"
                insert_daily_price_volume(ticker, new_date, interval, data[new_date]['1. open'], data[new_date]['2. high'], data[new_date]['3. low'], data[new_date]['4. close'], data[new_date]['5. volume'])
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Price/Volume data(" + url + ") NOT FOUND!!!... Moving to the next one!!!")

    else:
        last_run = get_status(ticker, interval=interval)
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            if interval == 'daily':
                start_date = datetime.datetime.strptime(DAILY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()
            elif interval == 'weekly':
                start_date = datetime.datetime.strptime(WEEKLY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()

            if last_run == None:
                last_run = start_date

            if new_date > start_date and new_date > last_run:
                insert_daily_price_volume(ticker, date, interval, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            else:
                break


def update_price_volume_data_for(ticker, api_key, interval, date):

    if interval == 'daily':
        interval_enum = 'TIME_SERIES_DAILY'
    elif interval == 'weekly':
        interval_enum = 'TIME_SERIES_WEEKLY'

    url = 'https://www.alphavantage.co/query?function={0}&symbol={1}&outputsize=full&apikey={2}'.format(interval_enum, ticker, api_key)

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        r = requests.get(url)

    response_data = r.json()
    data = response_data['Time Series (Daily)']

    print(str(datetime.datetime.now()) + ' : . Price/Volume data')
    if is_valid_date(date):
        try:
            try:
                update_daily_price_volume(ticker, date, interval, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            except:
                new_date = date+" 16:00:01"
                insert_daily_price_volume(ticker, new_date, interval, data[new_date]['1. open'], data[new_date]['2. high'], data[new_date]['3. low'], data[new_date]['4. close'], data[new_date]['5. volume'])
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Price/Volume data(" + url + ") NOT FOUND!!!... Moving to the next one!!!")

    else:
        last_run = get_status(ticker, interval=interval)
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            if interval == 'daily':
                start_date = datetime.datetime.strptime(DAILY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()
            elif interval == 'weekly':
                start_date = datetime.datetime.strptime(WEEKLY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()

            if last_run == None:
                last_run = start_date

            if new_date > start_date and new_date > last_run:
                update_daily_price_volume(ticker, date, interval, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            else:
                break


def process_stochastic_data_for(ticker, api_key, interval, date=None):

    url = 'https://www.alphavantage.co/query?function=STOCH&symbol={0}&interval={1}&apikey={2}'.format(ticker, interval, api_key)

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        r = requests.get(url)
    except requests.exceptions.ChunkedEncodingError:
        time.sleep(60)
        r = requests.get(url)

    response_data = r.json()
    data = response_data['Technical Analysis: STOCH']

    print(str(datetime.datetime.now()) + ' : . Stochastic data')
    if is_valid_date(date):
        try:
            try:
                update_daily_technicals_stochs(ticker, date, interval, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))
            except:
                new_date = date+" 16:00:01"
                update_daily_technicals_stochs(ticker, new_date, interval, data[new_date]['SlowK'], data[new_date]['SlowD'], (float(data[new_date]['SlowK']) - float(data[new_date]['SlowD'])))
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Stochastic data(" + url + ") NOT FOUND!!!... Moving to the next one!!!")

    else:
        last_run = get_status(ticker, interval=interval)
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            if interval == 'daily':
                start_date = datetime.datetime.strptime(DAILY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()
            elif interval == 'weekly':
                start_date = datetime.datetime.strptime(WEEKLY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()

            if last_run == None:
                last_run = start_date

            if new_date > start_date and new_date > last_run:
                update_daily_technicals_stochs(ticker, date, interval, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))
            else:
                break


def process_rsi_data_for(ticker, api_key, interval, date=None):

    url = 'https://www.alphavantage.co/query?function=RSI&symbol={0}&interval={1}&time_period=14&series_type=open&apikey={2}'.format(ticker, interval, api_key)

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        r = requests.get(url)

    response_data = r.json()
    data = response_data['Technical Analysis: RSI']

    print(str(datetime.datetime.now()) + ' : . RSI data')
    if is_valid_date(date):
        try:
            try:
                update_daily_technicals_rsi(ticker, date, interval, data[date]['RSI'])
            except:
                new_date = date+" 16:00:01"
                update_daily_technicals_rsi(ticker, new_date, interval, data[new_date]['RSI'])
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " RSI data(" + url + ") NOT FOUND!!!... Moving to the next one!!!")

    else:
        last_run = get_status(ticker, interval=interval)
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            if interval == 'daily':
                start_date = datetime.datetime.strptime(DAILY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()
            elif interval == 'weekly':
                start_date = datetime.datetime.strptime(WEEKLY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()

            if last_run == None:
                last_run = start_date

            if new_date > start_date and new_date > last_run:
                update_daily_technicals_rsi(ticker, date, interval, data[date]['RSI'])
            else:
                break

def process_ema_data_for(ticker, api_key, ema_period, interval, date=None):

    url = 'https://www.alphavantage.co/query?function=EMA&symbol={0}&interval={1}&time_period={2}&series_type=open&apikey={3}'.format(ticker, interval, ema_period, api_key)

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        r = requests.get(url)

    response_data = r.json()
    data = response_data['Technical Analysis: EMA']

    print(str(datetime.datetime.now()) + ' : . EMA-'+ str(ema_period) + ' data')
    if is_valid_date(date):
        ema_key = 'ema'+str(ema_period)
        try:
            try:
                ema_value = data[date]['EMA']
                update_daily_technicals_ema(ticker, date, interval, ema_key, ema_value)
            except:
                new_date = date+" 16:00:01"
                ema_value = data[new_date]['EMA']
                update_daily_technicals_ema(ticker, new_date, interval, ema_key, ema_value)
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " " + ema_key + "(" + url + ") NOT FOUND!!!... Moving to the next one!!!")
    else:
        last_run = get_status(ticker, interval=interval)
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            if interval == 'daily':
                start_date = datetime.datetime.strptime(DAILY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()
            elif interval == 'weekly':
                start_date = datetime.datetime.strptime(WEEKLY_DATA_COLLECTION_START_DATE, '%Y-%m-%d').date()

            if last_run == None:
                last_run = start_date

            if new_date > start_date and new_date > last_run:
                update_daily_technicals_ema(ticker, date, interval, 'ema'+str(ema_period), data[date]['EMA'])
            else:
                break


def process_fundamentals_for(ticker, api_key):
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={0}&apikey={1}'.format(ticker, api_key)

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(60)
        r = requests.get(url)

    response_data = r.json()
    if response_data:
        data = {}
        data['mcap'] = 0.0 if response_data['MarketCapitalization'] is None or response_data['MarketCapitalization'] == 'None' else response_data['MarketCapitalization']
        data['pe'] = 0.0 if response_data['PERatio'] is None or response_data['PERatio'] == 'None' else response_data['PERatio']
        data['pe_trailing'] = 0.0 if response_data['TrailingPE'] is None or response_data['TrailingPE'] == 'None' else response_data['TrailingPE']
        data['pe_forward'] = 0.0 if response_data['ForwardPE'] is None or response_data['ForwardPE'] == 'None' else response_data['ForwardPE']
        data['beta'] = 0.0 if response_data['Beta'] is None or response_data['Beta'] == 'None' else response_data['Beta']
        data['eps'] = 0.0 if response_data['EPS'] is None or response_data['EPS'] == 'None' else response_data['EPS']
        data['revenue'] = 0.0 if response_data['RevenueTTM'] is None or response_data['RevenueTTM'] == 'None' else response_data['RevenueTTM']
        data['high52week'] = 0.0 if response_data['52WeekHigh'] is None or response_data['52WeekHigh'] == 'None' else response_data['52WeekHigh']
        data['low52week'] = 0.0 if response_data['52WeekLow'] is None or response_data['52WeekLow'] == 'None' else response_data['52WeekLow']
        data['sma50'] = 0.0 if response_data['50DayMovingAverage'] is None or response_data['50DayMovingAverage'] == 'None' else response_data['50DayMovingAverage']
        data['sma200'] = 0.0 if response_data['200DayMovingAverage'] is None or response_data['200DayMovingAverage'] == 'None' else response_data['200DayMovingAverage']
        # cur.execute(sql, (ticker,date, data['mcap'], data['pe'], data['pe_forward'], data['pe_trailing'], data['revenue'], data['eps'], data['beta'], data['high52week'], data['low52week']))
        # print(str(data))
        insert_monthly_fundamentals(ticker=ticker, date=datetime.date.today().strftime('%Y-%m-%d'), data=data)

def process_ema8_data_for(ticker, api_key, interval, date=None):
    process_ema_data_for(ticker, api_key, ema_period=8, interval=interval, date=date)


def process_ema12_data_for(ticker, api_key, interval, date=None):
    process_ema_data_for(ticker, api_key, ema_period=12, interval=interval, date=date)


def process_ema200_data_for(ticker, api_key, interval, date=None):
    process_ema_data_for(ticker, api_key, ema_period=200, interval=interval, date=date)


def process_ema21_data_for(ticker, api_key, interval, date=None):
    process_ema_data_for(ticker, api_key, ema_period=21, interval=interval, date=date)


def process_ema50_data_for(ticker, api_key, interval, date=None):
    process_ema_data_for(ticker, api_key, ema_period=50, interval=interval, date=date)


def process_ema200_data_for(ticker, api_key, interval, date=None):
    process_ema_data_for(ticker, api_key, ema_period=200, interval=interval, date=date)

