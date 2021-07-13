import datetime
import psycopg2


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

def update_daily_technicals_rsi(ticker, date, rsi_value):
    sql = """UPDATE \"Tech_Daily\" SET rsi=%s
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


def update_daily_technicals_ema(ticker, date, ema_key, ema_value):

    if ema_key == 'ema8':
        sql = """UPDATE \"Tech_Daily\" SET ema8=%s
                 WHERE ticker=%s AND date=%s ;"""
    elif ema_key == 'ema9':
        sql = """UPDATE \"Tech_Daily\" SET ema9=%s
                 WHERE ticker=%s AND date=%s ;"""
    elif ema_key == 'ema12':
        sql = """UPDATE \"Tech_Daily\" SET ema12=%s
                 WHERE ticker=%s AND date=%s ;"""
    elif ema_key == 'ema13':
        sql = """UPDATE \"Tech_Daily\" SET ema13=%s
                 WHERE ticker=%s AND date=%s ;"""
    elif ema_key == 'ema200':
        sql = """UPDATE \"Tech_Daily\" SET ema200=%s
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
