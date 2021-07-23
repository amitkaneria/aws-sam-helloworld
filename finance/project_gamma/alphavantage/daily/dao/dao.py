import datetime
import psycopg2
from finance.project_gamma.alphavantage.daily.util.util import is_valid_date, next_business_day, previous_business_day, previous_week_business_day, last_business_day, date_business_day


def insert_daily_price_volume(ticker, date, interval, open, high, low, close, volume):

    if interval == 'daily':
        sql = """INSERT INTO \"Daily_Data\"(open, high, low, close, volume, ticker, date)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) ;"""
    elif interval == 'weekly':
        sql = """INSERT INTO \"Weekly_Data\"(open, high, low, close, volume, ticker, date)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) ;"""
    elif interval == '60min':
        sql = """INSERT INTO \"Hourly_Data\"(open, high, low, close, volume, ticker, datetime)
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


def update_daily_price_volume(ticker, date, interval, open, high, low, close, volume):


    if interval == 'daily':
        sql = """UPDATE \"Daily_Data\" SET open=%s, high=%s, low=%s, close=%s, volume=%s
                  WHERE ticker=%s and date=%s ;"""
    elif interval == 'weekly':
        sql = """UPDATE \"Weekly_Data\" SET open=%s, high=%s, low=%s, close=%s, volume=%s
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

def insert_daily_technicals_stochs(ticker, date, interval, stochs_slowk, stochs_slowd, stochs_delta):

    if interval == 'daily':
        sql = """INSERT INTO \"Daily_Data\"(ticker, date, stochs_slowk, stochs_slowd, stochs_delta)
                 VALUES(%s, %s, %s, %s, %s) ;"""
    elif interval == 'weekly':
        sql = """INSERT INTO \"Weekly_Data\"(ticker, date, stochs_slowk, stochs_slowd, stochs_delta)
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


def update_daily_technicals_stochs(ticker, date, interval, stochs_slowk, stochs_slowd, stochs_delta):

    if interval == 'daily':
        sql = """UPDATE \"Daily_Data\" SET stochs_slowk=%s, stochs_slowd=%s, stochs_delta=%s
                 WHERE ticker=%s AND date=%s ;"""
    elif interval == 'weekly':
        sql = """UPDATE \"Weekly_Data\" SET stochs_slowk=%s, stochs_slowd=%s, stochs_delta=%s
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

def update_daily_technicals_rsi(ticker, date, interval, rsi_value):

    if interval == 'daily':
        sql = """UPDATE \"Daily_Data\" SET rsi=%s
                 WHERE ticker=%s AND date=%s ;"""
    elif interval == 'weekly':
        sql = """UPDATE \"Weekly_Data\" SET rsi=%s
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
            sql = """UPDATE \"Daily_Data\" SET ema8=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema9':
            sql = """UPDATE \"Daily_Data\" SET ema9=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema12':
            sql = """UPDATE \"Daily_Data\" SET ema12=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema21':
            sql = """UPDATE \"Daily_Data\" SET ema21=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema200':
            sql = """UPDATE \"Daily_Data\" SET ema200=%s
                     WHERE ticker=%s AND date=%s ;"""
    elif interval == 'weekly':
        if ema_key == 'ema8':
            sql = """UPDATE \"Weekly_Data\" SET ema8=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema9':
            sql = """UPDATE \"Weekly_Data\" SET ema9=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema12':
            sql = """UPDATE \"Weekly_Data\" SET ema12=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema21':
            sql = """UPDATE \"Weekly_Data\" SET ema21=%s
                     WHERE ticker=%s AND date=%s ;"""
        elif ema_key == 'ema200':
            sql = """UPDATE \"Weekly_Data\" SET ema200=%s
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



def get_tickers(last_run_date, priority=None):

    if last_run_date == None:
        last_run_date = last_business_day(date=None)

    if priority == None:
        sql = """select ticker from public."WatchList" where daily_last_run_date < %s order by priority ;"""
    else:
        sql = """select ticker from public."WatchList" where hourly_last_run_date < %s AND priority = %s order by priority ;"""

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="Gamma", user='postgres', password='admin', host='127.0.0.1', port= '5432'
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
        sql = """SELECT daily_last_run_date FROM \"WatchList\"
                     WHERE ticker=%s ;"""
    elif interval == 'weekly':
        sql = """SELECT weekly_last_run_date FROM \"WatchList\"
                     WHERE ticker=%s ;"""

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
        sql = """INSERT INTO \"WatchList\"(ticker, daily_last_run_date)
                 VALUES(%s, %s) ;"""
    elif interval == 'weekly':
        sql = """INSERT INTO \"WatchList\"(ticker, weekly_last_run_date)
                 VALUES(%s, %s) ;"""

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
        sql = """UPDATE \"WatchList\" SET daily_last_run_date=%s
                     WHERE ticker=%s;"""
    elif interval == 'weekly':
        sql = """UPDATE \"WatchList\" SET weekly_last_run_date=%s
                     WHERE ticker=%s;"""
    elif interval == 'hourly':
        sql = """UPDATE \"WatchList\" SET hourly_last_run_date=%s
                     WHERE ticker=%s;"""

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
