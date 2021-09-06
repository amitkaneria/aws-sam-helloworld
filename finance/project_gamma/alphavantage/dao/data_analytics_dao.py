import datetime
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

postgres_db_server      = os.environ.get('POSTGRES.DB.SERVER')
postgres_db_port        = os.environ.get('POSTGRES.DB.PORT')
postgres_db_user        = os.environ.get('POSTGRES.DB.USER')
postgres_db_password    = os.environ.get('POSTGRES.DB.PASSWORD')
postgres_db_database    = os.environ.get('POSTGRES.DB.DATABASE')


def process_signals(start_date, end_date, method, buy_sell, interval='daily'):

    if datetime.datetime.strptime(str(start_date), '%Y-%m-%d').date() > datetime.date.today() \
            or (end_date != None and datetime.datetime.strptime(str(end_date), '%Y-%m-%d').date() > datetime.date.today()):
        print("Future Date not permitted!!!")
        return

    print(" # " + interval +" # " + method + " # " + buy_sell)
    option = interval+"_"+buy_sell+"_"+method

    if option == 'daily_buy_ema.8.12':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                        SELECT A.ticker, B.date, 'buy', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', B.close
                        FROM gamma.daily_data A, gamma.daily_data B
                        WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                            AND A.ema8 < A.ema12  AND B.ema8 > B.ema12
                        ON CONFLICT (ticker,date,method)
                        DO NOTHING
                        ;"""

    elif option == 'daily_sell_ema.8.12':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'sell', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND A.ema8 > A.ema12  AND B.ema8 < B.ema12
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_ema.21':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'EMA_21', 'EMA 21 crossing this week price for potential buy signal, please verify with other technicals and material news, ratings changes', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND A.close < A.ema21  AND B.close > B.ema21
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_ema.50':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'EMA_50', 'EMA 50 crossing this day price for potential buy signal, please verify with other technicals and material news, ratings changes', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND A.close < A.ema50  AND B.close > B.ema50
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_ema.200':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'EMA_200', 'EMA 200 crossing this week price for potential buy signal, please verify with other technicals and material news, ratings changes', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND A.close < A.ema200  AND B.close > B.ema200
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_sell_ema.21':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'sell', 'EMA_21', 'EMA 21 crossing this week price for potential sell signal, please verify with other technicals and material news, ratings changes', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND A.close > A.ema21  AND B.close < B.ema21
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_stoch.slow':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicated signal, Potential trend change. Please verify with other technicals as RSI/ EMA 21/ 8-12 crossover and material news, ratings changes', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND ((A.stochs_delta < 0 and B.stochs_delta > 0) OR ((B.stochs_delta - A.stochs_delta) > 10))
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_sell_stoch.slow':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'sell', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicates signal, Potential trend change. Please verify with other technicals as RSI/ EMA 21/ 8-12 crossover and material news, ratings changes', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker and A.date = %s and B.date = %s
                                AND ((A.stochs_delta > 0 and B.stochs_delta < 0) OR ((A.stochs_delta - B.stochs_delta) > 10)) 
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_rsi':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'RSI', 'RSI Oversold, please verify with other technicals and material news, ratings changes', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker and A.date = %s and B.date = %s
                                and A.rsi < 30 and B.rsi > A.rsi 
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_amit.special':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'AMIT.SP', 'Stochastic crossover with either RSI oversold, or in uptrend with price above EMA-21', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker and A.date = %s and B.date = %s
                                and A.stochs_delta < 0 and B.stochs_delta > 0 AND ((A.rsi < 30 and B.rsi > A.rsi) OR (B.ema21 > B.close OR B.ema8 > B.ema12)) 
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_sell_amit.special':
        sql = """INSERT INTO gamma.daily_signals (ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'sell', 'AMIT.SP', 'Stochastic crossover with either RSI oversold, or in uptrend with price above EMA-21', B.close
                            FROM gamma.daily_data A, gamma.daily_data B
                            WHERE A.ticker = B.ticker and A.date = %s and B.date = %s
                                and A.stochs_slowk < B.stochs_slowk AND A.stochs_slowd < B.stochs_slowd 
                                AND B.ema21 > B.close OR B.ema8 < B.ema12 
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'weekly_buy_ema.8.12':
        sql = """INSERT INTO gamma.weekly_signals (ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'buy', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', B.close
                    FROM gamma.weekly_data A, gamma.weekly_data B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.ema8 < A.ema12  AND B.ema8 > B.ema12
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_sell_ema.8.12':
        sql = """INSERT INTO gamma.weekly_signals (ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'sell', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', B.close
                    FROM gamma.weekly_data A, gamma.weekly_data B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.ema8 > A.ema12  AND B.ema8 < B.ema12
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_buy_ema.21':
        sql = """INSERT INTO gamma.weekly_signals (ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'buy', 'EMA_21', 'EMA 21 crossing this week price for potential buy signal, please verify with other technicals and material news, ratings changes', B.close
                    FROM gamma.weekly_data A, gamma.weekly_data B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.close < A.ema21  AND B.close > B.ema21
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_sell_ema.21':
        sql = """INSERT INTO gamma.weekly_signals (ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'sell', 'EMA_21', 'EMA 21 crossing this week price for potential sell signal, please verify with other technicals and material news, ratings changes', B.close
                    FROM gamma.weekly_data A, gamma.weekly_data B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.close > A.ema21  AND B.close < B.ema21
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_buy_stoch.slow':
        sql = """INSERT INTO gamma.weekly_signals (ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'buy', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicated signal, Potential trend change. Please verify with other technicals as RSI/ EMA 21/ 8-12 crossover and material news, ratings changes', B.close
                    FROM gamma.weekly_data A, gamma.weekly_data B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.stochs_delta < 0 and B.stochs_delta > 0 
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_sell_stoch.slow':
        sql = """INSERT INTO gamma.weekly_signals (ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'sell', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicates signal, Potential trend change. Please verify with other technicals as RSI/ EMA 21/ 8-12 crossover and material news, ratings changes', B.close
                    FROM gamma.weekly_data A, gamma.weekly_data B
                    where A.ticker = B.ticker and A.date = %s and B.date = %s
                    and A.stochs_delta > 0 and B.stochs_delta < 0 
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_buy_rsi':
        sql = """INSERT INTO gamma.weekly_signals(ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'buy', 'RSI', 'RSI Oversold, please verify with other technicals and material news, ratings changes', B.close
                    FROM gamma.weekly_data A, gamma.weekly_data B
                    WHERE A.ticker = B.ticker and A.date = %s and B.date = %s
                        and A.rsi < 30 and B.rsi > A.rsi 
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""


    else:
        print("WRONG OPTIONS! RETURNING ... ")

    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database=postgres_db_database, user=postgres_db_user, password=postgres_db_password, host=postgres_db_server, port=postgres_db_port
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (start_date, end_date))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
