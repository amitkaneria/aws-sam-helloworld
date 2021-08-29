import time
import datetime
from finance.project_gamma.alphavantage.api.api import process_price_volume_data_for, process_stochastic_data_for, process_ema8_data_for, \
    process_ema12_data_for, process_ema21_data_for, process_rsi_data_for, process_intraday_price_volume_data_for, process_data_for, generate_signal,\
    process_ema200_data_for, process_ema50_data_for
from finance.project_gamma.alphavantage.util.util import last_business_day, previous_business_day, next_business_day, \
    next_week_business_day, friday_before_previous_friday, previous_friday
from finance.project_gamma.alphavantage.dao.dao import update_status, get_tickers
from finance.project_gamma.alphavantage.dao.data_analytics_dao import process_signals
from dotenv import load_dotenv
import os
load_dotenv()

# 1	"MAIN"
# 2	"GROWTH"
# 4	"MEME"
# 6	"WEED"
# 7	"BITCOIN"
# 8	"CHINA"
# 10	"PIG"
# 11	"ARK"
# 12	"FIN"
# 13	"GIANTS"
# "MEME"

ticker_list_new     = ['SCHW', 'BNTX', 'CMG', 'JNJ', 'EFX', 'NVS', 'TXN', 'WHR']

#7/14
ticker_list_delta = ['UPST', 'HGV', 'APHA', 'FVRR', 'ADBE', 'AI']

################################################################################
API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')

option=1
print('Select Options below:' + str(option))
print('##### ##### ##### ##### #####')

## DEFAULT ##  for Multiple Ticker list, and for a given DATE, usually today's
## This updates all data for today's date (or any missing date data)
if option == 1:

    interval = 'daily'
    # ticker_list_db = get_tickers(interval=interval, last_run_date=None, priority=None)
    # ticker_list_db = get_tickers(last_run_date=None, priority=None)
    ticker_list_db = get_tickers(interval='daily', last_run_date=None, priority=0)
    print("Priority: 0, Running Daily for List:" + str(ticker_list_db))
    for ticker in ticker_list_db:
        print(str(datetime.datetime.now()) + ' : ##### ##### '+ ticker + ' ##### #####')
        # process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-07-16')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        process_data_for(ticker, api_key=API_KEY, interval=interval, date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(30)

    if len(ticker_list_db) > 0:
        # Daily Analytics Run
        generate_signal(interval='daily', start_date=str(previous_business_day(last_business_day(None))), end_date=None)
    else:
        print('NOTE: Analytics is not NOT for empty watch-list')
    print('##### ##### ##### ##### #####')

    ticker_list_db = get_tickers(interval='daily', last_run_date=None, priority=1)
    print("Priority: 1, Running Daily for List:" + str(ticker_list_db))
    for ticker in ticker_list_db:
        print(str(datetime.datetime.now()) + ' : ##### ##### '+ ticker + ' ##### #####')
        # process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-07-16')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        process_data_for(ticker, api_key=API_KEY, interval=interval, date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(25)

    if len(ticker_list_db) > 0:
        # Daily Analytics Run
        generate_signal(interval='daily', start_date=str(previous_business_day(last_business_day(None))), end_date=None)
    else:
        print('NOTE: Analytics is not NOT for empty watch-list')
    print('##### ##### ##### ##### #####')

    ticker_list_db = get_tickers(interval='daily', last_run_date=None, priority=2)
    print("Priority: 2, Running Daily for List:" + str(ticker_list_db))
    for ticker in ticker_list_db:
        print(str(datetime.datetime.now()) + ' : ##### ##### '+ ticker + ' ##### #####')
        # process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-07-16')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        process_data_for(ticker, api_key=API_KEY, interval=interval, date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(25)

    if len(ticker_list_db) > 0:
        # Daily Analytics Run
        generate_signal(interval='daily', start_date=str(previous_business_day(last_business_day(None))), end_date=None)
    else:
        print('NOTE: Analytics is not NOT for empty watch-list')
    print('##### ##### ##### ##### #####')

    ticker_list_db = get_tickers(interval=interval, last_run_date=None, priority=None)
    print("Priority: ALL, Running Daily for List:" + str(ticker_list_db))
    for ticker in ticker_list_db:
        print(str(datetime.datetime.now()) + ' : ##### ##### '+ ticker + ' ##### #####')
        # process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-07-16')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        process_data_for(ticker, api_key=API_KEY, interval=interval, date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(25)

    if len(ticker_list_db) > 0:
        # Daily Analytics Run
        generate_signal(interval='daily', start_date=str(previous_business_day(last_business_day(None))), end_date=None)
    else:
        print('NOTE: Analytics is not NOT for empty watch-list')
    print('##### ##### ##### ##### #####')

    ticker_list_db = get_tickers(interval='weekly', last_run_date=None, priority=None)
    print("Running Weekly for List:" + str(ticker_list_db))
    for ticker in ticker_list_db:
        print(str(datetime.datetime.now()) + ' : ##### ##### '+ ticker + ' ##### #####')
        # process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-07-16')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(25)

    if len(ticker_list_db) > 0:
        # Weekly Analytics Run
        generate_signal(interval='weekly', start_date=friday_before_previous_friday(), end_date=previous_friday())
    else:
        print('NOTE: Analytics is NOT run for empty watch-list')
    print('##### ##### ##### ##### #####')

## Daily Analytics Run
elif option == 2:
    # generate_signal(interval='daily', start_date=friday_before_previous_friday(), end_date=last_business_day())
    generate_signal(interval='daily', start_date='2020-12-31', end_date=last_business_day())

elif option == 3:

    # process_data_for("UPST", api_key=API_KEY, interval='weekly', date=None)
    # process_data_for("BNTX", api_key=API_KEY, interval='daily', date='2021-07-22')
    # process_data_for(ticker='SI', api_key=API_KEY, interval='daily', date=None)
    process_data_for(ticker='IRBT', api_key=API_KEY, interval='daily', date=None)
    # process_ema50_data_for(ticker='AAPL', api_key=API_KEY, interval='daily', date=None)

elif option == 4:
    # generate_signal(interval='weekly', start_date='2020-01-03', end_date='2020-12-25')
    # generate_signal(interval='daily', start_date='2020-12-31', end_date=None)
    generate_signal(interval='daily', start_date='2021-07-27', end_date='2021-08-02')

elif option == 5:
    # ticker_list_db = get_tickers(interval='daily', last_run_date='2021-07-21', priority=1)
    ticker_list_db = get_tickers(interval='daily', last_run_date=None, priority=None)
    print("Running for List:" + str(ticker_list_db))

elif option == 6:
    ticker_list_db = ['WISH', 'BBBY', 'NOK', 'CLOV', 'KODK', 'AMC', 'RKT', 'BIIB', 'GPRO', 'BB', 'GME', 'CRSR', 'SOFI', 'APHA', 'SNDL', 'RIOT', 'SI', 'MARA', 'MSTR', 'COIN', 'BIDU', 'GOTU', 'FUTU', 'BABA', 'BILI', 'U', 'GOCO', 'DM', 'PLUG', 'QS', 'SKLZ', 'LAZR', 'DDD', 'EDIT', 'ARKX', 'ARKW', 'VERV', 'TTD', 'PNC', 'MS', 'WFC', 'BLK', 'DPST', 'C', 'BAC', 'USB', 'DELL', 'EBAY', 'IBM', 'CSCO', 'ORCL', 'SAP', 'JNPR', 'INTC', 'TDOC', 'VIAC', 'HD', 'LMT', 'MILE', 'KTOS', 'ARKF', 'SQQQ', 'MU', 'TSP', 'CCIV', 'M', 'TIGR', 'XOM', 'CHWY', 'UPRO', 'GM', 'XM', 'UA', 'BA', 'CVS', 'ARKK', 'TRMB', 'ROOT', 'UNH', 'SPCE', 'CMCSA', 'NTLA', 'LUV', 'CCL', 'TLRY', 'NCLH', 'TMUS', 'FEYE', 'BEAM', 'CVNA', 'DAL', 'GLBE', 'SPXU', 'UPS', 'EXPR', 'FDX', 'CLDR', 'F', 'MA', 'LOW', 'ULTA', 'TSM', 'SDS', 'HGV', 'UAL', 'ADDYY', 'TGT', 'COST', 'SFIX', 'WMT', 'V', 'HLT', 'NKE', 'UPST', 'APP', 'PATH', 'OSTK', 'SH', 'PTON', 'RBLX', 'ARKG', 'LEVI', 'MAR', 'BYND']
    for ticker in ticker_list_db:
        process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-08-11')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        # process_data_for(ticker, api_key=API_KEY, interval=interval, date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(25)

    if len(ticker_list_db) > 0:
        # Daily Analytics Run
        generate_signal(interval='daily', start_date='2021-08-10', end_date=None)
    else:
        print('NOTE: Analytics is not NOT for empty watch-list')
    print('##### ##### ##### ##### #####')


else:
    print('Please select correct options: 1, 2, 3, 4, 5')

# ['GME', 'CRSR', 'SOFI', 'APHA', 'SNDL', 'RIOT', 'SI', 'MARA', 'MSTR', 'COIN', 'BIDU', 'GOTU', 'FUTU', 'BABA', 'BILI', 'U', 'GOCO', 'DM', 'PLUG', 'QS', 'SKLZ', 'LAZR', 'DDD', 'EDIT', 'ARKX', 'ARKW', 'VERV', 'TTD', 'PNC', 'MS', 'WFC', 'BLK', 'DPST', 'C', 'BAC', 'USB', 'DELL', 'EBAY', 'IBM', 'CSCO', 'ORCL', 'SAP', 'JNPR', 'INTC', 'TDOC', 'VIAC', 'HD', 'LMT', 'MILE', 'KTOS', 'ARKF', 'SQQQ', 'MU', 'TSP', 'CCIV', 'M', 'TIGR', 'XOM', 'CHWY', 'UPRO', 'GM', 'XM', 'UA', 'BA', 'CVS', 'ARKK', 'TRMB', 'ROOT', 'UNH', 'SPCE', 'CMCSA', 'NTLA', 'LUV', 'CCL', 'TLRY', 'NCLH', 'TMUS', 'FEYE', 'BEAM', 'CVNA', 'DAL', 'GLBE', 'SPXU', 'UPS', 'EXPR', 'FDX', 'CLDR', 'F', 'MA', 'LOW', 'ULTA', 'TSM', 'SDS', 'HGV', 'UAL', 'ADDYY', 'TGT', 'COST', 'SFIX', 'WMT', 'V', 'HLT', 'NKE', 'UPST', 'APP', 'PATH', 'OSTK', 'SH', 'PTON', 'RBLX', 'ARKG', 'LEVI', 'MAR', 'BYND']
# for date 8/11/2021