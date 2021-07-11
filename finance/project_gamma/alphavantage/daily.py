import time
from finance.project_gamma.alphavantage.api.api import process_price_volume_data_for, process_stochastic_data_for, process_ema8_data_for, process_ema12_data_for, process_ema200_data_for
from finance.project_gamma.alphavantage.util.util import is_valid_date

def process_data_for(ticker, api_key, date):
    process_price_volume_data_for(ticker, api_key=API_KEY, date=date)
    process_stochastic_data_for(ticker, api_key=API_KEY, date=date)
    process_ema8_data_for(ticker, api_key=API_KEY, date=date)
    process_ema12_data_for(ticker, api_key=API_KEY, date=date)
    process_ema200_data_for(ticker, api_key=API_KEY, date=date)
    # print('. . . . . sleeping for 1 min')
    # time.sleep(60)
    # update_vwap_data_for(ticker, api_key=API_KEY, date=date)
    # update_sma20_data_for(ticker, api_key=API_KEY, date=date)
    # update_sma50_data_for(ticker, api_key=API_KEY, date=date)
    # update_sma100_data_for(ticker, api_key=API_KEY, date=date)
    # update_sma200_data_for(ticker, api_key=API_KEY, date=date)

ticker_list_etf             = ['SPY', 'QQQ', 'DIA']
ticker_list_tech_behemoths  = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'FB', 'TWTR', 'NFLX', 'AMD', 'NVDA', 'CRM', 'ADBE', 'NOW']
ticker_list_tech_titans     = ['IBM', 'CSCO', 'INTC', 'DELL', 'IBM']
ticker_list_tech_streaming  = ['NFLX', 'ROKU', 'DIS', 'ZM', 'FUBO', 'CMCSA', 'VIAC', 'SNAP' ]
ticker_list_tech_chips      = ['NVDA', 'AMD',  'INTC', 'QCOM']
ticker_list_tech_insurance  = ['LMND', 'GOCO', 'MILE', 'ROOT' ]
ticker_list_tech_database   = ['MDB', 'AI', 'PLTR', 'DOCU', 'SNOW', 'SPLK', 'ESTC', 'FROG', 'NOW', 'DDOG']
ticker_list_tech_security   = ['CRWD',  ]
ticker_list_tech_network    = ['FSLY', 'NET', 'ZS', 'CSCO', 'JNPR'  ]
ticker_list_tech_shopping   = ['SHOP', 'AMZN', 'DASH', 'ABNB', 'W', 'ETSY' ]
ticker_list_tech_gaming     = ['U', 'RBLX'  ]
ticker_list_tech_software   = ['FVRR', 'UPWK', 'XM', 'TWLO' ]
ticker_list_tech_re         = ['Z', 'OPEN', 'RDFN'  ]
ticker_list_tech_fin        = ['PYPL', 'SQ', 'COIN'  ]
ticker_list_tech_betting    = ['DKNG', 'PENN', 'CRSR', 'LVS'  ]
ticker_list_china           = ['BABA', 'BIDU', 'NIO' ]
ticker_list_tech_bio        = ['NVAX', 'BEAM', 'NTLA', 'MRNA', 'TDOC']
ticker_list_fin             = ['JPM', 'GS', 'BAC', 'WFC', 'DPST', 'TIGR', 'UPST']
ticker_list_transport       = ['FDX', 'UPS']
ticker_list_consumer        = ['M', 'NKE', 'LEVI', 'WMT', 'UA', 'ADDYY', 'BYND', 'OSTK', 'PTON' ]
ticker_list_tech_mfg        = ['DM', 'DDD' ]
ticker_list_housing         = ['HD', 'LOW']
ticker_list_cars            = ['F', 'GM', 'TSLA', 'NIO']
ticker_list_meme            = ['GME', 'AMC', 'BBBY', 'CLOV', 'GPRO']
ticker_list_weed            = ['SNDL', 'APHA']
ticker_list_ark_funds       = ['SPCE', 'KTON']
ticker_list_energy          = []

# ticker_list_new1 = ['UA', 'ADDYY', 'BYND', 'DM', 'DDD', 'LVS', 'OSTK', 'IBM', 'CSCO', 'INTC', 'JNPR', 'QCOM', 'PTON', 'SPCE', 'KTOS', 'TWLO', 'DELL']
# ticker_list_new2 = ['LRCX', 'WBA', 'SKLZ', 'APPS', 'APP', 'WISH', 'TLRY', 'APHA', 'CCIV', 'FUBO', 'LAZR', 'NOK', 'KODK', 'BIIB', 'BB']
# ticker_list_new2 = ['WBA', 'SKLZ', 'APPS', 'APP', 'WISH', 'TLRY', 'APHA', 'CCIV', 'FUBO', 'LAZR', 'NOK', 'KODK', 'BIIB', 'BB']
ticker_list_new3 = [ 'APXT', 'PSAC', 'TNX', 'TSP', 'EDIT', 'VERV', 'CHWY', 'BA', 'UBER', 'LYFT', 'CLDR', 'RKT', 'GLBE', 'TGT', 'COST', 'ARKG', 'ARKK']
ticker_list_new4 = ['ARKW', 'ARKX', 'BAH', 'CYBR', 'EBAY', 'FEYE', 'FUTU', 'JMIA', 'MA', 'OKTA', 'PINS', 'PLUG', 'QS', 'RIOT', 'MARA', 'SFIX', 'MU']
ticker_list_new5 = ['SOS', 'SPOT', 'TRMB', 'TTD', 'V', 'WIX', 'X', 'PATH', 'XOM', 'GOTU', 'BILI', 'CARV', 'SAP', 'ORCL', 'MAR', 'HLT', 'HGV']
ticker_list_new6 = ['WH', 'UAL', 'DAL', 'LUV', 'CCL', 'NCLH', 'EXPR', 'AXP', 'PETS', ]

API_KEY='XYF81MAS06D29A24'

option=4
print('Select Options below:' + str(option))

# USE Option#1 ## DEFAULT ##  for Multiple Ticker list, and for a given DATE, usually today's
if option == 1:

    ticker_list = [ticker_list_etf, ticker_list_tech_bio, ticker_list_tech_fin, ticker_list_tech_mfg, ticker_list_tech_re, ticker_list_tech_chips,
                   ticker_list_tech_betting, ticker_list_tech_database, ticker_list_tech_gaming, ticker_list_tech_network, ticker_list_tech_security,
                   ticker_list_tech_shopping, ticker_list_tech_software, ticker_list_tech_titans, ticker_list_tech_behemoths, ticker_list_tech_insurance,
                   ticker_list_tech_streaming, ticker_list_china, ticker_list_fin, ticker_list_transport, ticker_list_consumer, ticker_list_housing,
                   ticker_list_cars, ticker_list_meme, ticker_list_weed, ticker_list_ark_funds, ticker_list_energy]

    for sub_ticker_list in ticker_list:
        for ticker in sub_ticker_list:
            process_data_for(ticker, api_key=API_KEY, date='2021-07-09')
            time.sleep(60)

# USE Option#2 ## for single ticker, and for a given DATE
elif option == 2:

    ticker = 'AMZN'
    today_flag = False

    process_data_for(ticker, api_key=API_KEY, date='2021-07-09')

# USE Option#3 ## for multiple ticker, and for a given DATE
elif option == 3:

    counter=1
    for ticker in ticker_list_new:
        if counter%5 == 0:
            time.sleep(60)
        counter = counter+1
        # process_data_for(ticker, api_key=API_KEY, date='2021-07-09')
        process_data_for(ticker, api_key=API_KEY, date=None)

# USE Option#4 ## DEFAULT for newly monitored ticker List ##  for Multiple Ticker list
elif option == 4:

    ticker_list = [ticker_list_new2, ticker_list_new3, ticker_list_new4, ticker_list_new6]

    for sub_ticker_list in ticker_list:
        for ticker in sub_ticker_list:
            process_data_for(ticker, api_key=API_KEY, date=None)
            time.sleep(60)

    #########################################################################
    # THIS IS TEMP, PLEASE REMOVE AFTER FRIDAY 7/9 RUN
    ticker_list = [ticker_list_etf, ticker_list_tech_bio, ticker_list_tech_fin, ticker_list_tech_mfg, ticker_list_tech_re, ticker_list_tech_chips,
                   ticker_list_tech_betting, ticker_list_tech_database, ticker_list_tech_gaming, ticker_list_tech_network, ticker_list_tech_security,
                   ticker_list_tech_shopping, ticker_list_tech_software, ticker_list_tech_titans, ticker_list_tech_behemoths, ticker_list_tech_insurance,
                   ticker_list_tech_streaming, ticker_list_china, ticker_list_fin, ticker_list_transport, ticker_list_consumer, ticker_list_housing,
                   ticker_list_cars, ticker_list_meme, ticker_list_weed, ticker_list_ark_funds, ticker_list_energy]

    for sub_ticker_list in ticker_list:
        for ticker in sub_ticker_list:
            process_data_for(ticker, api_key=API_KEY, date='2021-07-09')
            time.sleep(60)
    #########################################################################

else:

    print('Please correct options: 1, 2, 3, 4')