import requests
import datetime
import psycopg2
from dateutil.parser import parse
import time

def is_valid_date(date):
    if date:
        try:
            parse(date)
            return True
        except:
            return False
    return False


def insert_daily_price_volume(ticker, date, open, high, low, close, volume):
    sql = """INSERT INTO \"Tech_Daily\"(open, high, low, close, volume, ticker, date)
             VALUES(%s, %s, %s, %s, %s, %s, %s) ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='admin', host='127.0.0.1', port= '5432'
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (open, high, low, close, volume, ticker, date))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_daily_price_volume(ticker, date, open, high, low, close, volume):
    sql = """UPDATE \"Tech_Daily\" SET open=%s, high=%s, low=%s, close=%s, volume=%s
              WHERE ticker=%s and date=%s ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='admin', host='127.0.0.1', port= '5432'
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (open, high, low, close, volume, ticker, date))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




def process_price_volume_data_for(ticker, api_key, date=None):

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&outputsize=full&apikey={1}'.format(ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Time Series (Daily)']

    # today = datetime.date.today()
    # todate = today.strftime("%Y-%m-%d")

    print('Running Ticker: ' + ticker)
    if is_valid_date(date):
        print(date)
        update_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])
    else:
        for date in data:
            print(date)
            new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            date_2015 = datetime.datetime.strptime('2015-12-31', '%Y-%m-%d').date()
            if new_date > date_2015:
                update_daily_price_volume(ticker, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume'])


ticker_list_tech = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'FB', 'TWTR', 'NFLX', 'TSLA', 'ROKU', 'PYPL', 'SQ', 'AMD', 'NVDA', 'NIO', 'BIDU', 'BABA', 'COIN', 'JPM', 'LMND', 'AI', 'MDB', 'PLTR', 'ZM', 'FSLY', 'NET', 'CMCSA', 'VIAC', 'U', 'RBLX', 'OPEN', 'RDFN', 'Z', 'SHOP', 'DOCU', 'CRWD', 'ZS', 'DASH', 'ABNB', 'FROG', 'SNOW', 'SPLK', 'ESTC', 'SNAP', 'CRM', 'ADBE', 'NOW', 'FVRR', 'UPWK', 'MILE', 'ROOT', 'GOCO', 'XM']
ticker_list_bio = ['NVAX', 'BEAM', 'NTLA', 'MRNA', 'TDOC']
ticker_list_fin = ['JPM', 'GS', 'BAC', 'WFC', 'DPST', 'TIGR', 'UPST']
ticker_list_transport = ['FDX', 'UPS']
ticker_list_consumer = ['M', 'NKE', 'UA']
ticker_list_housing = ['HD', 'LOW']
ticker_list_cars = ['F', 'GM', 'TSLA', 'NIO']
ticker_list_meme = ['GME', 'AMC', 'BBBY', 'CLOV']
ticker_list_ark_funds = ['']
ticker_list_energy = ['']

Print('Select Options below:')
option=1

if option == 1:

    ticker = 'AMZN'
    API_KEY='XYF81MAS06D29A24'
    today_flag = False

    process_price_volume_data_for(ticker, api_key=API_KEY)

elif option == 2:

    counter=1
    for ticker in ticker_list_tech:
        if counter%5 == 0:
            time.sleep(60)
        counter = counter+1
        # process_price_volume_data_for(key, api_key=API_KEY, date='2021-07-07')
        process_price_volume_data_for(ticker, api_key=API_KEY)

elif option == 3:

    counter=1
    ticker_list = [ticker_list_tech, ticker_list_bio, ticker_list_fin, ticker_list_transport, ticker_list_consumer, ticker_list_housing,
                   ticker_list_cars, ticker_list_meme, ticker_list_ark_funds, ticker_list_energy]

    for sub_ticker_list in ticker_list:
        for ticker in sub_ticker_list:
            if counter%5 == 0:
                time.sleep(60)
            counter = counter+1
            # process_price_volume_data_for(key, api_key=API_KEY, date='2021-07-07')
            process_price_volume_data_for(ticker, api_key=API_KEY)

else:

    print('Please correct options: 1, 2, 3')