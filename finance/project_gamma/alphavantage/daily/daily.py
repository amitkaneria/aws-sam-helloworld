import time
import datetime
from finance.project_gamma.alphavantage.daily.api.api import process_price_volume_data_for, process_stochastic_data_for, process_ema8_data_for, process_ema12_data_for, process_ema21_data_for, update_price_volume_data_for, process_rsi_data_for, process_intraday_price_volume_data_for
from finance.project_gamma.alphavantage.daily.util.util import is_valid_date, last_business_day, date_business_day, previous_business_day, next_business_day, previous_week_business_day, next_week_business_day, friday_before_previous_friday, previous_friday
from finance.project_gamma.alphavantage.daily.dao.dao import update_status, insert_status, get_status, get_tickers
from finance.project_gamma.alphavantage.daily.dao.data_analytics_dao import process_signals

def process_data_for(ticker, api_key, interval, date):

    print(str(datetime.datetime.now()) + ' : ##### ##### '+ ticker + ' ##### #####')

    ## Pricing Data
    if interval == 'daily' or interval == 'weekly':
        process_price_volume_data_for(ticker, api_key=API_KEY, interval=interval, date=date)
    elif interval == '60min':
        process_intraday_price_volume_data_for(ticker, api_key=API_KEY, interval=interval, date=date)

    ## Stochastic Daya
    process_stochastic_data_for(ticker, api_key=API_KEY, interval=interval, date=date)

    ## EMA-8 Data
    process_ema8_data_for(ticker, api_key=API_KEY, interval=interval, date=date)

    ## EMA-12 Data
    process_ema12_data_for(ticker, api_key=API_KEY, interval=interval, date=date)

    print(str(datetime.datetime.now()) + ' : . . . sleeping')
    time.sleep(20)

    ## EMA-21 Data
    process_ema21_data_for(ticker, api_key=API_KEY, interval=interval, date=date)

    ## RSI Data
    process_rsi_data_for(ticker, api_key=API_KEY, interval=interval, date=date)
    ###### process_ema200_data_for(ticker, api_key=API_KEY, interval=interval, date=date)

    ###### Update DB Status
    # insert_status(ticker, interval=interval, date=datetime.datetime.now().strftime("%Y-%m-%d"))
    update_status(ticker, interval=interval, date=datetime.datetime.now().strftime("%Y-%m-%d"))


def generate_signal(interval='daily', start_date='2020-12-31', end_date=None):

    if end_date == None:
        end_date = datetime.date.today()
    # else:
    #     end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    if interval == 'daily':
        next_business_date = next_business_day(start_date)
    elif interval == 'weekly':
        next_business_date = next_week_business_day(start_date)

    print("##### Generating Report for Interval :" + interval)
    while next_business_date <= datetime.date.today() and next_business_date <= end_date:

        print("##### START DATE : " + str(start_date) + " , ## END DATE : " + str(next_business_date))

        ## Potential trend change indicators
        process_signals(start_date, end_date=next_business_date, interval=interval, method='stoch.slow', buy_sell='buy')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='stoch.slow', buy_sell='sell')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='rsi', buy_sell='buy')
        # process_signals(start_date, end_date=next_business_date, interval=interval, method='rsi', buy_sell='sell')

        ## Strong trend indicators
        process_signals(start_date, end_date=next_business_date, interval=interval, method='ema.8.12', buy_sell='buy')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='ema.8.12', buy_sell='sell')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='ema.21', buy_sell='buy')
        process_signals(start_date, end_date=next_business_date, interval=interval, method='ema.21', buy_sell='sell')

        ## Special Indicators
        # process_signals(start_date, end_date=next_business_date, interval=interval, method='amit.special', buy_sell='buy')
        # process_signals(start_date, end_date=next_business_date, interval=interval, method='amit.special', buy_sell='sell')

        start_date = next_business_date
        if interval == 'daily':
            next_business_date = next_business_day(start_date)
        elif interval == 'weekly':
            next_business_date = next_week_business_day(start_date)


#1 - Giants, Leaders
#2 - Upcoming tech companies, high beta LMND, MDB, ZM, ZS
#3 - Biotech
#8 - China
#9 - meme
#10 - bitcoin
#11 -
#12 - finance
#13 - tech blue chips


ticker_list_new     = ['SCHW', 'BNTX', 'CMG', 'JNJ', 'EFX', 'NVS', 'TXN', 'WHR']

#7/14
ticker_list_delta = ['UPST', 'HGV', 'APHA', 'FVRR', 'ADBE', 'AI']

################################################################################
API_KEY='XYF81MAS06D29A24'

option=1
print('Select Options below:' + str(option))

## DEFAULT ##  for Multiple Ticker list, and for a given DATE, usually today's
## This updates all data for today's date (or any missing date data)
if option == 1:

    interval = 'daily'
    ticker_list_db = get_tickers(interval=interval, last_run_date=None, priority=None)
    # ticker_list_db = get_tickers(last_run_date=None, priority=None)
    print("Running Daily for List:" + str(ticker_list_db))
    for ticker in ticker_list_db:
        # process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-07-16')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        process_data_for(ticker, api_key=API_KEY, interval=interval, date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(25)

    # Daily Analytics Run
    generate_signal(interval='daily', start_date=str(previous_business_day(last_business_day(None))), end_date=None)

    ticker_list_db = get_tickers(interval='weekly', last_run_date=None, priority=None)
    print("Running Weekly for List:" + str(ticker_list_db))
    for ticker in ticker_list_db:
        # process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-07-16')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(25)


    # Weekly Analytics Run
    generate_signal(interval='weekly', start_date=friday_before_previous_friday(), end_date=previous_friday())

## Daily Analytics Run
elif option == 2:
    generate_signal(interval='daily', start_date=friday_before_previous_friday(), end_date=last_business_day())


elif option == 3:

        # process_data_for("UPST", api_key=API_KEY, interval='weekly', date=None)
    process_data_for("BNTX", api_key=API_KEY, interval='daily', date='2021-07-22')


elif option == 4:
    # generate_signal(interval='weekly', start_date='2020-01-03', end_date='2020-12-25')
    generate_signal(interval='daily', start_date='2020-12-31', end_date='2021-07-20')


elif option == 5:
    ticker_list_db = get_tickers(last_run_date='2021-07-21', priority=1)
    print("Running for List:" + str(ticker_list_db))


else:
    print('Please select correct options: 1, 2, 3, 4')

