import requests
import datetime
from finance.project_gamma.alphavantage.dao.dao import insert_daily_price_volume, insert_daily_technicals_stochs, update_daily_price_volume, update_daily_technicals_stochs, update_daily_technicals_ema
from finance.project_gamma.alphavantage.util.util import is_valid_date


def process_price_volume_data_for(ticker, api_key, date):

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&outputsize=full&apikey={1}'.format(ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Time Series (Daily)']

    print('Ticker: ' + ticker + ' Price/Volume data ... ')
    if is_valid_date(date):
        print(ticker + '::' +date)
        insert_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
    else:
        for date in data:
            # print(ticker + '::' +date)
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            date_2015 = datetime.datetime.strptime('2015-12-31', '%Y-%m-%d').date()
            if new_date > date_2015:
                insert_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
            else:
                break


def process_stochastic_data_for(ticker, api_key, date=None):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=STOCH&symbol={0}&interval=daily&apikey={1}'.format(ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Technical Analysis: STOCH']

    print('Running Ticker: ' + ticker + ' Stochastic data ... ')
    if is_valid_date(date):
        print(ticker + '::' +date)
        update_daily_technicals_stochs(ticker, date, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))
    else:
        for date in data:
            # print(ticker + '::' +date)
            try:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except:
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()

            date_2015 = datetime.datetime.strptime('2015-12-31', '%Y-%m-%d').date()
            if new_date > date_2015:
                update_daily_technicals_stochs(ticker, date, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))
            else:
                break

def process_ema_data_for(ticker, api_key, ema_period, date=None):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=EMA&symbol={0}&interval=daily&time_period={1}&series_type=open&apikey={2}'.format(ticker, ema_period, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Technical Analysis: EMA']

    print('Running Ticker: ' + ticker + ' EMA '+ str(ema_period) + 'data ... ')
    if is_valid_date(date):
        print(ticker + '::' +date)
        update_daily_technicals_ema(ticker, date, 'ema'+str(ema_period), data[date]['EMA'])
    else:
        for date in data:
            # print(ticker + '::' +date)
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

