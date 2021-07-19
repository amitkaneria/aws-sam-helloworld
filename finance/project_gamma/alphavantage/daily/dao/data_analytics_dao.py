import datetime
import psycopg2
from finance.project_gamma.alphavantage.daily.util.util import is_valid_date, next_business_day, previous_business_day, previous_week_business_day

def process_ema_8_12_buy_signals(date, interval='daily'):

    if datetime.datetime.strptime(str(date), '%Y-%m-%d').date() > datetime.date.today():
        print("Future Date not permitted!!!")
        return

    if interval == 'daily':
        start_date = previous_business_day(date)
        sql = """INSERT INTO public."Weekly_Signals"(ticker, date, buy_sell, method, note, reco_price)
                SELECT A.ticker, B.date, 'buy', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicates signal, please verify with other technicals and material news, ratings changes', B.close
                FROM public."Weekly_Data" A, public."Weekly_Data" B
                WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                    AND (A.stochs_delta < 0 and B.stochs_delta > 0  and A.stochs_slowk < 65)
                ;"""
    elif interval == 'weekly':
        start_date = previous_week_business_day(date)
        sql = """INSERT INTO public."Weekly_Signals"(ticker, date, buy_sell, method, note, reco_price)
                SELECT A.ticker, B.date, 'buy', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicates signal, please verify with other technicals and material news, ratings changes', B.close
                FROM public."Weekly_Data" A, public."Weekly_Data" B
                WHERE A.ticker = B.ticker AND A.date = %s AND B.date = %s
                    AND (A.stochs_delta < 0 and B.stochs_delta > 0  and A.stochs_slowk < 65)
                ;"""

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
        cur.execute(sql, (start_date, date))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
