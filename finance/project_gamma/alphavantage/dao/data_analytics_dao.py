import datetime
import psycopg2


def process_signals(start_date, end_date, method, buy_sell, interval='daily'):

    if datetime.datetime.strptime(str(start_date), '%Y-%m-%d').date() > datetime.date.today() \
            or (end_date != None and datetime.datetime.strptime(str(end_date), '%Y-%m-%d').date() > datetime.date.today()):
        print("Future Date not permitted!!!")
        return

    print(" # " + interval +" # " + method + " # " + buy_sell)
    option = interval+"_"+buy_sell+"_"+method

    if option == 'daily_buy_ema.8.12':
        sql = """INSERT INTO public."Daily_Signals"(ticker, date, buy_sell, method, note, reco_price)
                        SELECT A.ticker, B.date, 'buy', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', B.close
                        FROM public."Daily_Data" A, public."Daily_Data" B
                        WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                            AND A.ema8 < A.ema12  AND B.ema8 > B.ema12
                        ON CONFLICT (ticker,date,method)
                        DO NOTHING
                        ;"""

    elif option == 'daily_sell_ema.8.12':
        sql = """INSERT INTO public."Daily_Signals"(ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'sell', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', B.close
                            FROM public."Daily_Data" A, public."Daily_Data" B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND A.ema8 > A.ema12  AND B.ema8 < B.ema12
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_ema.21':
        sql = """INSERT INTO public."Daily_Signals"(ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'EMA_21', 'EMA 21 crossing this week price for potential buy signal, please verify with other technicals and material news, ratings changes', B.close
                            FROM public."Daily_Data" A, public."Daily_Data" B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND A.close < A.ema21  AND B.close > B.ema21
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_sell_ema.21':
        sql = """INSERT INTO public."Daily_Signals"(ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'sell', 'EMA_21', 'EMA 21 crossing this week price for potential sell signal, please verify with other technicals and material news, ratings changes', B.close
                            FROM public."Daily_Data" A, public."Daily_Data" B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND A.close > A.ema21  AND B.close < B.ema21
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_stoch.slow':
        sql = """INSERT INTO public."Daily_Signals"(ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicated signal, Potential trend change. Please verify with other technicals as RSI/ EMA 21/ 8-12 crossover and material news, ratings changes', B.close
                            FROM public."Daily_Data" A, public."Daily_Data" B
                            WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                                AND ((A.stochs_delta < 0 and B.stochs_delta > 0) OR ((B.stochs_delta - A.stochs_delta) > 10))
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_sell_stoch.slow':
        sql = """INSERT INTO public."Daily_Signals"(ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'sell', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicates signal, Potential trend change. Please verify with other technicals as RSI/ EMA 21/ 8-12 crossover and material news, ratings changes', B.close
                            FROM public."Daily_Data" A, public."Daily_Data" B
                            WHERE A.ticker = B.ticker and A.date = %s and B.date = %s
                                AND ((A.stochs_delta > 0 and B.stochs_delta < 0) OR ((A.stochs_delta - B.stochs_delta) > 10)) 
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_rsi':
        sql = """INSERT INTO public."Daily_Signals"(ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'RSI', 'RSI Oversold, please verify with other technicals and material news, ratings changes', B.close
                            FROM public."Daily_Data" A, public."Daily_Data" B
                            WHERE A.ticker = B.ticker and A.date = %s and B.date = %s
                                and A.rsi < 30 and B.rsi > A.rsi 
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_buy_amit.special':
        sql = """INSERT INTO public."Daily_Signals"(ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'buy', 'AMIT.SP', 'Stochastic crossover with either RSI oversold, or in uptrend with price above EMA-21', B.close
                            FROM public."Daily_Data" A, public."Daily_Data" B
                            WHERE A.ticker = B.ticker and A.date = %s and B.date = %s
                                and A.stochs_delta < 0 and B.stochs_delta > 0 AND ((A.rsi < 30 and B.rsi > A.rsi) OR (B.ema21 > B.close OR B.ema8 > B.ema12)) 
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'daily_sell_amit.special':
        sql = """INSERT INTO public."Daily_Signals"(ticker, date, buy_sell, method, note, reco_price)
                            SELECT A.ticker, B.date, 'sell', 'AMIT.SP', 'Stochastic crossover with either RSI oversold, or in uptrend with price above EMA-21', B.close
                            FROM public."Daily_Data" A, public."Daily_Data" B
                            WHERE A.ticker = B.ticker and A.date = %s and B.date = %s
                                and A.stochs_slowk < B.stochs_slowk AND A.stochs_slowd < B.stochs_slowd 
                                AND B.ema21 > B.close OR B.ema8 < B.ema12 
                            ON CONFLICT (ticker,date,method)
                            DO NOTHING
                            ;"""

    elif option == 'weekly_buy_ema.8.12':
        sql = """INSERT INTO public."Weekly_Signals"(ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'buy', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', B.close
                    FROM public."Weekly_Data" A, public."Weekly_Data" B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.ema8 < A.ema12  AND B.ema8 > B.ema12
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_sell_ema.8.12':
        sql = """INSERT INTO public."Weekly_Signals"(ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'sell', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', B.close
                    FROM public."Weekly_Data" A, public."Weekly_Data" B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.ema8 > A.ema12  AND B.ema8 < B.ema12
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_buy_ema.21':
        sql = """INSERT INTO public."Weekly_Signals"(ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'buy', 'EMA_21', 'EMA 21 crossing this week price for potential buy signal, please verify with other technicals and material news, ratings changes', B.close
                    FROM public."Weekly_Data" A, public."Weekly_Data" B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.close < A.ema21  AND B.close > B.ema21
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_sell_ema.21':
        sql = """INSERT INTO public."Weekly_Signals"(ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'sell', 'EMA_21', 'EMA 21 crossing this week price for potential sell signal, please verify with other technicals and material news, ratings changes', B.close
                    FROM public."Weekly_Data" A, public."Weekly_Data" B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.close > A.ema21  AND B.close < B.ema21
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_buy_stoch.slow':
        sql = """INSERT INTO public."Weekly_Signals"(ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'buy', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicated signal, Potential trend change. Please verify with other technicals as RSI/ EMA 21/ 8-12 crossover and material news, ratings changes', B.close
                    FROM public."Weekly_Data" A, public."Weekly_Data" B
                    WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                        AND A.stochs_delta < 0 and B.stochs_delta > 0 
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_sell_stoch.slow':
        sql = """INSERT INTO public."Weekly_Signals"(ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'sell', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicates signal, Potential trend change. Please verify with other technicals as RSI/ EMA 21/ 8-12 crossover and material news, ratings changes', B.close
                    FROM public."Weekly_Data" A, public."Weekly_Data" B
                    where A.ticker = B.ticker and A.date = %s and B.date = %s
                    and A.stochs_delta > 0 and B.stochs_delta < 0 
                    ON CONFLICT (ticker,date,method)
                    DO NOTHING
                    ;"""

    elif option == 'weekly_buy_rsi':
        sql = """INSERT INTO public."Weekly_Signals"(ticker, date, buy_sell, method, note, reco_price)
                    SELECT A.ticker, B.date, 'buy', 'RSI', 'RSI Oversold, please verify with other technicals and material news, ratings changes', B.close
                    FROM public."Weekly_Data" A, public."Weekly_Data" B
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
            database="Gamma", user='postgres', password='IFSTdNN6XB9MLt2vFyXI', host='wallstdata.ctgi8zbyshxe.us-east-1.rds.amazonaws.com', port= '5432'
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
