import requests
import json
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

apikey = 'ULK4W4HT2V7UIIIS'
ticker = 'LMND'

response = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=LMND&apikey=ULK4W4HT2V7UIIIS")
#logging.warning(response)
logging.warning(response.text)
#print(json.loads(response.text))

response_data = json.loads(response.text)

data = {}
data['low'] = response_data['52WeekLow']
data['high'] = response_data['52WeekHigh']
data['sma50'] = response_data['50DayMovingAverage']
data['sma200'] = response_data['200DayMovingAverage']


daily_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=LMND&apikey=ULK4W4HT2V7UIIIS'
response = requests.get(daily_url)
response_data = json.loads(response.text)

data['last_close'] = response_data['Time Series (Daily)']['2021-05-28']['4. close']
down_percent = float(data['last_close'])/ float(data['high'])
data['down_percent_from_52WeekHigh'] = down_percent

logging.warning('Ticker: {0}, 52WeekHigh: {1}, 52WeekLow: {2}, 50sma: {3}, 200sma: {4}, Last Close: {5}, Down from High: {6}'.format(ticker, data['low'], data['high'], data['sma50'], data['sma200'], data['last_close'], data['down_percent_from_52WeekHigh']))
