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


def insert_daily_technicals_stochs(ticker, date, stochs_slowk, stochs_slowd, stochs_delta):
    sql = """INSERT INTO \"Tech_Daily\"(ticker, date, stochs_slowk, stochs_slowd, stochs_delta)
             VALUES(%s, %s, %s, %s, %s) ;"""
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
        cur.execute(sql, (ticker,date,stochs_slowk, stochs_slowd, stochs_delta))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_daily_technicals_stochs(ticker, date, stochs_slowk, stochs_slowd, stochs_delta):
    sql = """UPDATE \"Tech_Daily\" SET stochs_slowk=%s, stochs_slowd=%s, stochs_delta=%s
             WHERE ticker=%s AND date=%s ;"""
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
        cur.execute(sql, (stochs_slowk, stochs_slowd, stochs_delta, ticker,date))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def process_stochastic_data_for(ticker, api_key, date=None):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=STOCH&symbol={0}&interval=daily&apikey={1}'.format(ticker, api_key)

    r = requests.get(url)
    response_data = r.json()
    data = response_data['Technical Analysis: STOCH']

    today = datetime.date.today()
    todate = today.strftime("%Y-%m-%d")
    ##print("d1 =", d1)

    ##print(data['Technical Analysis: STOCH'][d1])

    print('Running Ticker: ' + ticker)
    if is_valid_date(date):
        print(date)
        update_daily_technicals_stochs(ticker, date, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))
    else:
        for date in data:
            print(date)
            new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            date_2015 = datetime.datetime.strptime('2015-12-31', '%Y-%m-%d').date()
            if new_date > date_2015:
                update_daily_technicals_stochs(ticker, date, data[date]['SlowK'], data[date]['SlowD'], (float(data[date]['SlowK']) - float(data[date]['SlowD'])))


ticker_list_tech = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'FB', 'TWTR', 'NFLX', 'TSLA', 'ROKU', 'PYPL', 'SQ', 'AMD', 'NVDA', 'NIO', 'BIDU', 'BABA', 'COIN', 'JPM', 'LMND', 'AI', 'MDB', 'PLTR', 'ZM', 'FSLY', 'NET', 'CMCSA', 'VIAC', 'U', 'RBLX', 'OPEN', 'RDFN', 'Z', 'SHOP', 'DOCU', 'CRWD', 'ZS', 'DASH', 'ABNB', 'FROG', 'SNOW', 'SPLK', 'ESTC', 'SNAP', 'CRM', 'ADBE', 'NOW', 'FVRR', 'UPWK', 'MILE', 'ROOT', 'GOCO']
ticker_list_bio = ['NVAX', 'BEAM', 'NTLA', 'MRNA', 'TDOC']
ticker_list_fin = ['JPM', 'GS', 'BAC', 'WFC', 'DPST', 'TIGR', 'UPST']
ticker_list_transport = ['FDX', 'UPS', ]
ticker_list_consumer = ['M', 'NKE']
ticker_list_housing = ['HD', 'LOW']
ticker_list_cars = ['F', 'GM', 'TSLA', 'NIO']
ticker_list_meme = ['GME', 'AMC', 'BBBY', 'CLOV', 'NEGG']
ticker_list_ark_funds = []
ticker_list_energy = []

API_KEY='XYF81MAS06D29A24'

print('Select Options below:')
option=3

if option == 1:

    ticker = 'AMZN'
    today_flag = False

    process_stochastic_data_for(ticker, api_key=API_KEY)

elif option == 2:

    counter=1
    for ticker in ticker_list_tech:
        if counter%5 == 0:
            time.sleep(60)
        counter = counter+1
        # process_stochastic_data_for(key, api_key=API_KEY, date='2021-07-07')
        process_stochastic_data_for(ticker, api_key=API_KEY)

elif option == 3:

    counter=1
    ticker_list = [ticker_list_tech, ticker_list_bio, ticker_list_fin, ticker_list_transport, ticker_list_consumer, ticker_list_housing,
                   ticker_list_cars, ticker_list_meme, ticker_list_ark_funds, ticker_list_energy]

    for sub_ticker_list in ticker_list:
        for ticker in sub_ticker_list:
            if counter%5 == 0:
                print('sleeping for 1 min')
                time.sleep(60)
            counter = counter+1
            process_stochastic_data_for(key, api_key=API_KEY, date='2021-07-07')

elif option == 4:

    counter=1
    # ticker_list = [ticker_list_tech, ticker_list_bio, ticker_list_fin, ticker_list_transport, ticker_list_consumer, ticker_list_housing,
    #                ticker_list_cars, ticker_list_meme, ticker_list_ark_funds, ticker_list_energy]
    ticker_list = [ticker_list_housing, ticker_list_cars, ticker_list_meme, ticker_list_ark_funds, ticker_list_energy]

    for sub_ticker_list in ticker_list:
        for ticker in sub_ticker_list:
            if counter%5 == 0:
                print('sleeping for 1 min')
                time.sleep(60)
            counter = counter+1
            # process_stochastic_data_for(key, api_key=API_KEY, date='2021-07-07')
            process_stochastic_data_for(ticker, api_key=API_KEY)

else:

    print('Please correct options: 1, 2, 3')