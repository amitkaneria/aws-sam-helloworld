import datetime

ticker='CRWD'
url = 'https://www.alphavantage.co/query?function=STOCH&symbol={0}&interval=daily&apikey={1}'.format(ticker, 12)
# url.replace('TICKER', ticker)
print(url)

# date = 'datetime'
# print(datetime.datetime.strptime(date, '%Y-%m-%d').date())

from dateutil.parser import parse
def is_valid_date(date):
    if date:
        try:
            parse(date)
            return True
        except:
            return False
    return False

print(is_valid_date('datetime'))