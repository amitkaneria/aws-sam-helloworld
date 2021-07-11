import requests

apikey = 'ULK4W4HT2V7UIIIS'
ticker = 'AAPL'

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=ULK4W4HT2V7UIIIS")
print(response)
print(response.text)

#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
