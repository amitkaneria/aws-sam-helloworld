import time
import datetime
from finance.project_gamma.alphavantage.daily.api.api import process_price_volume_data_for, process_stochastic_data_for, process_ema8_data_for, process_ema12_data_for, process_ema21_data_for, update_price_volume_data_for, process_rsi_data_for
from finance.project_gamma.alphavantage.daily.util.util import is_valid_date, last_business_day, date_business_day, previous_business_day, next_business_day, previous_week_business_day, next_week_business_day
from finance.project_gamma.alphavantage.daily.dao.dao import update_status, insert_status, get_status, get_tickers
from finance.project_gamma.alphavantage.daily.dao.data_analytics_dao import process_signals

def process_data_for(ticker, api_key, interval, date):
    print(str(datetime.datetime.now()) + ' : ##### ##### '+ ticker + ' ##### #####')
    process_price_volume_data_for(ticker, api_key=API_KEY, interval=interval, date=date)
    process_stochastic_data_for(ticker, api_key=API_KEY, interval=interval, date=date)
    process_ema8_data_for(ticker, api_key=API_KEY, interval=interval, date=date)
    process_ema12_data_for(ticker, api_key=API_KEY, interval=interval, date=date)
    print(str(datetime.datetime.now()) + ' : . . . sleeping')
    time.sleep(20)
    process_ema21_data_for(ticker, api_key=API_KEY, interval=interval, date=date)
    process_rsi_data_for(ticker, api_key=API_KEY, interval=interval, date=date)
    ###### process_ema200_data_for(ticker, api_key=API_KEY, interval=interval, date=date)

    ###### Update DB Status
    # insert_status(ticker, interval=interval, date=datetime.datetime.now().strftime("%Y-%m-%d"))
    update_status(ticker, interval=interval, date=datetime.datetime.now().strftime("%Y-%m-%d"))

def generate_signal(interval='daily', start_date='2020-12-31', end_date=None):

    if end_date == None:
        end_date = datetime.date.today()
    else:
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

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


# ticker_list_etf             = ['SPY', 'QQQ', 'DIA', 'SQQQ', 'SPXU', 'SDS', 'SH', 'UPRO']
# ticker_list_tech_behemoths  = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'FB', 'TWTR', 'NFLX', 'AMD', 'NVDA', 'CRM', 'ADBE', 'NOW']
# ticker_list_tech_titans     = ['IBM', 'CSCO', 'INTC', 'DELL', 'SAP', 'ORCL']
# ticker_list_tech_streaming  = ['NFLX', 'ROKU', 'DIS', 'ZM', 'FUBO', 'CMCSA', 'VIAC', 'SNAP', 'PINS', 'SPOT' ]
# ticker_list_tech_chips      = ['NVDA', 'AMD',  'INTC', 'QCOM', 'LRCX', 'MU', 'TSM']
# ticker_list_tech_insurance  = ['LMND', 'GOCO', 'MILE', 'ROOT' ]
# ticker_list_tech_database   = ['MDB', 'AI', 'PLTR', 'DOCU', 'SNOW', 'SPLK', 'ESTC', 'FROG', 'NOW', 'DDOG', 'CLDR']
# ticker_list_tech_security   = ['CRWD', 'CYBR', 'FEYE', 'OKTA' ]
# ticker_list_tech_network    = ['FSLY', 'NET', 'ZS', 'CSCO', 'JNPR', 'VZ', 'TMUS', 'T'  ]
# ticker_list_tech_shopping   = ['SHOP', 'AMZN', 'DASH', 'ABNB', 'W', 'ETSY', 'CHWY', 'GLBE', 'EBAY', 'JMIA', 'WIX', 'MELI' ]
# ticker_list_tech_gaming     = ['U', 'RBLX', 'SKLZ',   ]
# ticker_list_tech_software   = ['FVRR', 'UPWK', 'XM', 'TWLO', 'APPS', 'APP', 'APXT', 'PATH' ]
# ticker_list_tech_re         = ['Z', 'OPEN', 'RDFN', 'PSAC'  ]
# ticker_list_tech_fin        = ['PYPL', 'SQ', 'COIN', 'SOFI', 'MA', 'V', 'TTD', 'AXP'  ]
# ticker_list_tech_betting    = ['DKNG', 'PENN', 'CRSR', 'LVS'  ]
# ticker_list_china           = ['BABA', 'BIDU', 'NIO', 'FUTU', 'GOTU', 'BILI' ]
# ticker_list_tech_bio        = ['NVAX', 'BEAM', 'NTLA', 'MRNA', 'TDOC', 'BIIB', 'EDIT', 'VERV']
# ticker_list_pharma          = ['WBA', 'CVS', 'UNH']
# ticker_list_fin             = ['JPM', 'GS', 'MS', 'BAC', 'WFC', 'DPST', 'TIGR', 'UPST','C', 'BLK', 'PNC', 'USB', 'BK']
# ticker_list_transport       = ['FDX', 'UPS']
# ticker_list_consumer        = ['M', 'NKE', 'LEVI', 'WMT', 'UA', 'ADDYY', 'BYND', 'OSTK', 'PTON', 'TGT', 'COST', 'SFIX', 'EXPR', 'PETS', 'LULU', 'ULTA' ]
# ticker_list_staple          = ['PEP', 'KO' ]
# ticker_list_tech_mfg        = ['DM', 'DDD' ]
# ticker_list_housing         = ['HD', 'LOW']
# ticker_list_cars            = ['F', 'GM', 'TSLA', 'NIO', 'CCIV', 'WH', 'LAZR', 'TSP', 'PLUG', 'QS', 'CARV', 'WH']
# ticker_list_meme            = ['GME', 'AMC', 'BBBY', 'CLOV', 'GPRO', 'WISH', 'NOK', 'KODK', 'BB', 'RKT']
# ticker_list_weed            = ['SNDL', 'TLRY', 'APHA']
# ticker_list_ark_funds       = ['ARKG', 'ARKF', 'ARKK', 'ARKW', 'ARKX', 'SPCE', 'KTOS', 'TRMB']
# ticker_list_energy          = ['XOM']
# ticker_list_travel          = ['BA', 'UBER', 'LYFT', 'MAR', 'HLT', 'HGV', 'UAL', 'DAL', 'LUV', 'CCL', 'NCLH']
# ticker_list_govt            = ['BAH', 'X', 'LMT']
# ticker_list_blockchain      = ['RIOT', 'MARA', 'SOS']

#1 - Giants, Leaders
#2 - Upcoming tech companies, high beta LMND, MDB, ZM, ZS
#3 - Biotech
#8 - China
#9 - meme
#10 - bitcoin
#11 -

ticker_list_new     = ['AA', 'HDB', 'SCHW', 'ERIC', 'STT', 'BNTX']
ticker_list_new1    = ['UBS', 'CMG', 'TRV', 'IBKR', 'TER', 'PCAR', 'HAL', 'ALLY', 'CIT', 'JNJ', 'ANTM', 'CSX', 'EFX', 'NVS', 'TXN', 'WHR']

#7/14
ticker_list_delta = ['UPST', 'HGV', 'APHA', 'FVRR', 'ADBE', 'AI']

################################################################################
API_KEY='XYF81MAS06D29A24'

option=4
print('Select Options below:' + str(option))

## DEFAULT ##  for Multiple Ticker list, and for a given DATE, usually today's
## This updates all data for today's date (or any missing date data)
if option == 1:

    ticker_list_db = get_tickers(last_run_date=None)
    print("Running for List:" + str(ticker_list_db))
    for ticker in ticker_list_db:
        # process_data_for(ticker, api_key=API_KEY, interval='daily', date='2021-07-16')
        # process_data_for(ticker, api_key=API_KEY, interval='weekly', date=None)
        process_data_for(ticker, api_key=API_KEY, interval='daily', date=None)
        print(str(datetime.datetime.now()) + ' : . . . sleeping')
        time.sleep(25)

elif option == 2:

        # process_data_for("UPST", api_key=API_KEY, interval='weekly', date=None)
    process_data_for("UPST", api_key=API_KEY, interval='daily', date=None)

## Daily Analytics Run
elif option == 3:
    generate_signal(interval='daily', start_date=str(previous_business_day(last_business_day(None))), end_date=str(last_business_day(None)))

elif option == 4:
    # generate_signal(interval='weekly', start_date='2020-01-03', end_date='2020-12-25')
    # generate_signal(interval='daily', start_date='2020-01-03', end_date='2020-12-25')
    # generate_signal(interval='daily', start_date='2020-12-31', end_date='2021-07-20')
    generate_signal(interval='daily', start_date='2020-12-31', end_date='2021-07-20')
    # generate_signal(date=None, interval='weekly')

else:
    print('Please correct options: 1, 2, 3, 4')