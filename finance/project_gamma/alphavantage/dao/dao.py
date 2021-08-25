import psycopg2
from finance.project_gamma.alphavantage.util.util import last_business_day, previous_friday


def insert_daily_price_volume(ticker, date, interval, open, high, low, close, volume):

    if interval == 'daily':
        sql = """INSERT INTO gamma.daily_data(open, high, low, close, volume, ticker, date)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) ;"""
    elif interval == 'weekly':
        sql = """INSERT INTO gamma.weekly_data(open, high, low, close, volume, ticker, date)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) ;"""
    elif interval == '60min':
        sql = """INSERT INTO gamma.hourly_data(open, high, low, close, volume, ticker, datetime)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
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


def update_daily_price_volume(ticker, date, interval, open, high, low, close, volume):


    if interval == 'daily':
        sql = """UPDATE gamma.daily_data SET open=%s, high=%s, low=%s, close=%s, volume=%s
                  WHERE ticker=%s and date=%s ;"""
    elif interval == 'weekly':
        sql = """UPDATE gamma.weekly_data SET open=%s, high=%s, low=%s, close=%s, volume=%s
                  WHERE ticker=%s and date=%s ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
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

def insert_daily_technicals_stochs(ticker, date, interval, stochs_slowk, stochs_slowd, stochs_delta):

    if interval == 'daily':
        sql = """INSERT INTO gamma.daily_data (ticker, date, stochs_slowk, stochs_slowd, stochs_delta)
                 VALUES(%s, %s, %s, %s, %s) ;"""
    elif interval == 'weekly':
        sql = """INSERT INTO gamma.weekly_data (ticker, date, stochs_slowk, stochs_slowd, stochs_delta)
                 VALUES(%s, %s, %s, %s, %s) ;"""


    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
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


def update_daily_technicals_stochs(ticker, date, interval, stochs_slowk, stochs_slowd, stochs_delta):

    if interval == 'daily':
        sql = """UPDATE gamma.daily_data SET stochs_slowk=%s, stochs_slowd=%s, stochs_delta=%s
                 WHERE ticker=%s AND date=%s ;"""
    elif interval == 'weekly':
        sql = """UPDATE gamma.weekly_data SET stochs_slowk=%s, stochs_slowd=%s, stochs_delta=%s
                 WHERE ticker=%s AND date=%s ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
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

def update_daily_technicals_rsi(ticker, date, interval, rsi_value):

    if interval == 'daily':
        sql = """UPDATE gamma.daily_data SET rsi=%s
                 WHERE ticker=%s AND date=%s ;"""
    elif interval == 'weekly':
        sql = """UPDATE gamma.weekly_data SET rsi=%s
                 WHERE ticker=%s AND date=%s ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (rsi_value, ticker,date))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_daily_technicals_ema(ticker, date, interval, ema_key, ema_value):

    if interval == 'daily':
        if ema_key == 'ema8':
            sql = """UPDATE gamma.daily_data SET ema8=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema9':
            sql = """UPDATE gamma.daily_data SET ema9=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema12':
            sql = """UPDATE gamma.daily_data SET ema12=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema21':
            sql = """UPDATE gamma.daily_data SET ema21=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema200':
            sql = """UPDATE gamma.daily_data SET ema200=%s
                     WHERE ticker=%s AND date=%s ;"""
    elif interval == 'weekly':
        if ema_key == 'ema8':
            sql = """UPDATE gamma.weekly_data SET ema8=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema9':
            sql = """UPDATE gamma.weekly_data SET ema9=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema12':
            sql = """UPDATE gamma.weekly_data SET ema12=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema21':
            sql = """UPDATE gamma.weekly_data SET ema21=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema200':
            sql = """UPDATE gamma.weekly_data SET ema200=%s
                     WHERE ticker=%s AND date=%s ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (ema_value, ticker,date))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



def get_tickers(interval, last_run_date, priority=None):

    if interval == 'weekly' and last_run_date == None:
        last_run_date = previous_friday()
    elif interval == 'daily':
        last_run_date = last_business_day(date=None)
    else:
        last_run_date = last_run_date

    print('Running for Date: ' + str(last_run_date))

    if priority == None:
        if interval == 'daily':
            sql = """select ticker from gamma.watchlist where daily_last_run_date < %s order by priority ;"""
        elif interval == 'weekly':
            sql = """select ticker from gamma.watchlist where weekly_last_run_date < %s order by priority ;"""
        elif interval == '60min':
            sql = """select ticker from gamma.watchlist where hourly_last_run_date < %s order by priority ;"""
    else:
        if interval == 'daily':
            sql = """select ticker from gamma.watchlist where daily_last_run_date < %s AND priority = %s order by priority ;"""
        elif interval == 'weekly':
            sql = """select ticker from gamma.watchlist where weekly_last_run_date < %s AND priority = %s order by priority ;"""
        elif interval == '60min':
            sql = """select ticker from gamma.watchlist where hourly_last_run_date < %s AND priority = %s order by priority ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
        )
        cur = conn.cursor()
        if priority == None:
            cur.execute(sql, (last_run_date,))
        else:
            cur.execute(sql, (last_run_date, priority))
        ticker_list = []
        rows = cur.fetchall()
        for row in rows:
            ticker_list.append(row[0])
        # # commit the changes to the database
        # conn.commit()
        # close communication with the database
        cur.close()
        return ticker_list
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None
    finally:
        if conn is not None:
            conn.close()


def get_status(ticker, interval):

    if interval == 'daily':
        sql = """SELECT daily_last_run_date FROM gamma.watchlist
                     WHERE ticker=%s ;"""
    elif interval == 'weekly':
        sql = """SELECT weekly_last_run_date FROM gamma.watchlist
                     WHERE ticker=%s ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        # cur.execute(sql, (date, ticker))
        cur.execute(sql, (ticker,))
        last_run = None
        if cur.rowcount > 0:
            row = cur.fetchone()
            last_run = row[0]
        # # commit the changes to the database
        # conn.commit()
        # close communication with the database
        cur.close()
        return last_run
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None
    finally:
        if conn is not None:
            conn.close()


def insert_status(ticker, date, interval):

    if interval == 'daily':
        sql = """INSERT INTO gamma.watchlist(ticker, daily_last_run_date)
                 VALUES(%s, %s) ;"""
    elif interval == 'weekly':
        sql = """INSERT INTO gamma.watchlist(ticker, weekly_last_run_date)
                 VALUES(%s, %s) ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        # cur.execute(sql, (date, ticker))
        cur.execute(sql, (ticker,date))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_status(ticker, date, interval):

    if interval == 'daily':
        sql = """UPDATE gamma.watchlist SET daily_last_run_date=%s
                     WHERE ticker=%s;"""
    elif interval == 'weekly':
        sql = """UPDATE gamma.watchlist SET weekly_last_run_date=%s
                     WHERE ticker=%s;"""
    elif interval == 'hourly':
        sql = """UPDATE gamma.watchlist SET hourly_last_run_date=%s
                     WHERE ticker=%s;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (date, ticker))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
