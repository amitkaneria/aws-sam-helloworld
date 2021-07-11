# Imports
from pandas_datareader import data as pdr
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
import datetime
import time
yf.pdr_override()

# Variables
# tickers = si.tickers_sp500()
tickers = si.get_undervalued_large_caps()
print(tickers)