import requests
import datetime
from finance.project_gamma.alphavantage.daily.dao.dao import insert_daily_price_volume, insert_daily_technicals_stochs, update_daily_price_volume, update_daily_technicals_stochs, update_daily_technicals_ema, update_daily_technicals_rsi
from finance.project_gamma.alphavantage.daily.util.util import is_valid_date


def process_price_volume_data_for(ticker, api_key, interval, date):

    if interval == 'daily':
        interval_enum = 'TIME_SERIES_DAILY'

    url = 'https://www.alphavantage.co/query?function={0}&symbol={1}&outputsize=full&apikey={2}'.format(interval_enum, ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Time Series (Daily)']

    print(str(datetime.datetime.now()) + ' : . Price/Volume data')
    if is_valid_date(date):
        try:
            try:
                insert_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            except:
                new_date = date+" 16:00:01"
                insert_daily_price_volume(ticker, new_date, data[new_date]['1. open'], data[new_date]['2. high'], data[new_date]['3. low'], data[new_date]['4. close'], data[new_date]['5. volume'])
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Price/Volume data(" + url + ") NOT FOUND!!!... Moving to the next one!!!")

    else:
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            date_2015 = datetime.datetime.strptime('2015-12-31', '%Y-%m-%d').date()
            if new_date > date_2015:
                insert_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            else:
                break

def update_price_volume_data_for(ticker, api_key, interval, date):

    if interval == 'daily':
        interval_enum = 'TIME_SERIES_DAILY'

    url = 'https://www.alphavantage.co/query?function={0}&symbol={1}&outputsize=full&apikey={2}'.format(interval_enum, ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Time Series (Daily)']

    print(str(datetime.datetime.now()) + ' : . Price/Volume data')
    if is_valid_date(date):
        try:
            try:
                update_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            except:
                new_date = date+" 16:00:01"
                insert_daily_price_volume(ticker, new_date, data[new_date]['1. open'], data[new_date]['2. high'], data[new_date]['3. low'], data[new_date]['4. close'], data[new_date]['5. volume'])
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Price/Volume data(" + url + ") NOT FOUND!!!... Moving to the next one!!!")

    else:
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            date_2015 = datetime.datetime.strptime('2015-12-31', '%Y-%m-%d').date()
            if new_date > date_2015:
                update_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            else:
                break


def process_stochastic_data_for(ticker, api_key, interval, date=None):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=STOCH&symbol={0}&interval={1}&apikey={2}'.format(ticker, interval, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Technical Analysis: STOCH']

    print(str(datetime.datetime.now()) + ' : . Stochastic data')
    if is_valid_date(date):
        try:
            try:
                update_daily_technicals_stochs(ticker, date, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))
            except:
                new_date = date+" 16:00:01"
                update_daily_technicals_stochs(ticker, new_date, data[new_date]['SlowK'], data[new_date]['SlowD'], (float(data[new_date]['SlowK']) - float(data[new_date]['SlowD'])))
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Stochastic data(" + url + ") NOT FOUND!!!... Moving to the next one!!!")

    else:
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            date_2015 = datetime.datetime.strptime('2015-12-31', '%Y-%m-%d').date()
            if new_date > date_2015:
                update_daily_technicals_stochs(ticker, date, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))
            else:
                break


def process_rsi_data_for(ticker, api_key, interval, date=None):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=RSI&symbol={0}&interval={1}&time_period=10&series_type=open&apikey={2}'.format(ticker, interval, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Technical Analysis: RSI']

    print(str(datetime.datetime.now()) + ' : . RSI data')
    if is_valid_date(date):
        try:
            try:
                update_daily_technicals_rsi(ticker, date, data[date]['RSI'])
            except:
                new_date = date+" 16:00:01"
                update_daily_technicals_rsi(ticker, new_date, data[new_date]['RSI'])
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " RSI data(" + url + ") NOT FOUND!!!... Moving to the next one!!!")

    else:
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            date_2015 = datetime.datetime.strptime('2015-12-31', '%Y-%m-%d').date()
            if new_date > date_2015:
                update_daily_technicals_rsi(ticker, date, data[date]['RSI'])
            else:
                break

def process_ema_data_for(ticker, api_key, ema_period, interval, date=None):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=EMA&symbol={0}&interval={1}&time_period={2}&series_type=open&apikey={3}'.format(ticker, interval, ema_period, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Technical Analysis: EMA']

    print(str(datetime.datetime.now()) + ' : . EMA-'+ str(ema_period) + ' data')
    if is_valid_date(date):
        ema_key = 'ema'+str(ema_period)
        try:
            try:
                ema_value = data[date]['EMA']
                update_daily_technicals_ema(ticker, date, ema_key, ema_value)
            except:
                new_date = date+" 16:00:01"
                ema_value = data[new_date]['EMA']
                update_daily_technicals_ema(ticker, new_date, ema_key, ema_value)
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " " + ema_key + "(" + url + ") NOT FOUND!!!... Moving to the next one!!!")
    else:
        for date in data:
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            date_2015 = datetime.datetime.strptime('2015-12-31', '%Y-%m-%d').date()
            if new_date > date_2015:
                update_daily_technicals_ema(ticker, date, 'ema'+str(ema_period), data[date]['EMA'])
            else:
                break


def process_ema8_data_for(ticker, api_key, interval, date=None):
    process_ema_data_for(ticker, api_key, ema_period=8, interval=interval, date=date)


def process_ema12_data_for(ticker, api_key, interval, date=None):
    process_ema_data_for(ticker, api_key, ema_period=12, interval=interval, date=date)


def process_ema200_data_for(ticker, api_key, interval, date=None):
    process_ema_data_for(ticker, api_key, ema_period=200, interval=interval, date=date)

