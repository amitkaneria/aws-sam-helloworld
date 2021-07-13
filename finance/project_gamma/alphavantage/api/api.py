import requests
import datetime
from finance.project_gamma.alphavantage.dao.dao import insert_daily_price_volume, insert_daily_technicals_stochs, update_daily_price_volume, update_daily_technicals_stochs, update_daily_technicals_ema, update_daily_technicals_rsi
from finance.project_gamma.alphavantage.util.util import is_valid_date


def process_price_volume_data_for(ticker, api_key, date):

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&outputsize=full&apikey={1}'.format(ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Time Series (Daily)']

    if is_valid_date(date):
        try:
            insert_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Price/Volume data NOT FOUND!!!... Moving to the next one!!!")

    else:
        print(str(datetime.datetime.now()) + ' : ' + ticker + ' Price/Volume data ... ')
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

def update_price_volume_data_for(ticker, api_key, date):

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&outputsize=full&apikey={1}'.format(ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Time Series (Daily)']

    if is_valid_date(date):
        try:
            update_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Price/Volume data NOT FOUND!!!... Moving to the next one!!!")

    else:
        print(str(datetime.datetime.now()) + ' : ' + ticker + ' Price/Volume data ... ')
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


def process_stochastic_data_for(ticker, api_key, date=None):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=STOCH&symbol={0}&interval=daily&apikey={1}'.format(ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Technical Analysis: STOCH']

    if is_valid_date(date):
        try:
            update_daily_technicals_stochs(ticker, date, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " Stochastic data NOT FOUND!!!... Moving to the next one!!!")

    else:
        print(str(datetime.datetime.now()) + ' : ' + ticker + ' Stochastic data ... ')
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


def process_rsi_data_for(ticker, api_key, date=None):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=RSI&symbol={0}&interval=daily&time_period=10&series_type=open&apikey={1}'.format(ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Technical Analysis: RSI']

    if is_valid_date(date):
        try:
            update_daily_technicals_stochs(ticker, date, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " RSI data NOT FOUND!!!... Moving to the next one!!!")

    else:
        print(str(datetime.datetime.now()) + ' : ' + ticker + ' RSI data ... ')
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

def process_ema_data_for(ticker, api_key, ema_period, date=None):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=EMA&symbol={0}&interval=daily&time_period={1}&series_type=open&apikey={2}'.format(ticker, ema_period, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Technical Analysis: EMA']

    if is_valid_date(date):
        ema_key = 'ema'+str(ema_period)
        try:
            ema_value = data[date]['EMA']
            update_daily_technicals_ema(ticker, date, ema_key, ema_value)
        except:
            print(str(datetime.datetime.now()) + " : WARNING --- Ticker: " + ticker + " Date: " + date + " " + ema_key + " NOT FOUND!!!... Moving to the next one!!!")
    else:
        print(str(datetime.datetime.now()) + ' : ' + ticker + ' EMA-'+ str(ema_period) + ' data ... ')
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


def process_ema8_data_for(ticker, api_key, date=None):
    process_ema_data_for(ticker, api_key, ema_period=8, date=date)


def process_ema12_data_for(ticker, api_key, date=None):
    process_ema_data_for(ticker, api_key, ema_period=12, date=date)


def process_ema200_data_for(ticker, api_key, date=None):
    process_ema_data_for(ticker, api_key, ema_period=200, date=date)

