import psycopg2

def insert_vendor(date,fund,company,ticker,cusip,shares,marketvalue,weight):
    sql = """INSERT INTO \"ARK\"(date,fund,company,ticker,cusip,shares,marketvalue,weight, closing_price)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) ;"""
    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            # **params
            database="ARK_Analytics", user='postgres', password='admin', host='127.0.0.1', port= '5432'
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        if ticker == '':
            ticker = company
        cur.execute(sql, (date,fund,company,ticker,cusip,shares,marketvalue,weight, float(marketvalue)/shares))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # insert one vendor
    insert_vendor("1/8/2021", "ARKK", "ORGANOVO HOLDINGS INC", "ONVO", "68620A203", 781085.00, 9982266.30, 0.05)