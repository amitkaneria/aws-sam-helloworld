stock_fundamentals
##########################
ticker
IPO_date
category
52_week_high
52_week_low
avg_volume
market_cap

Technical_Daily
#########################
ticker
date
rsi
open
high
low
close
volume
volume_change%
up_%
stochS_slowd
stochS_slowk
stochS_delta
stochS_new
stochF_slowd
stochF_slowk
stochF_delta
stochF_new
ema9
ema12
ema_12_9
ema_12_9_new
vwap

tickers to watch
#####################
category (index)
ticker
category

## S&P 500  		-- 500
## Nasdaq 			-- 100
## Russell 2000		-- 2000
## Russell 1000		-- 1000
## year-2021-ipo	-- 500
## year-2020-ipo	-- 500

Levels
########################
ticker
resistance/support
levels


signals
########################
date
ticker
buy_sell
note


1. program that captures data for each above category
1a. rsi
1b. stoch
1c. ema9
1d. ema12
1e. volume

2. Query
2a. rsi values
2b. stochf +/-
2c. volume%
2d. stochs +/-

3. Query Signals Data
3a. Email/ SMS

---- Tech daily
SELECT * FROM public."Tech_Daily"
where ticker = 'AAPL' and date > '2021-01-01'
ORDER BY ticker ASC, date desc 

---- Stochastic Buy
insert into public."Signals"(ticker, date, buy_sell, method, note, reco_price)
SELECT A.ticker, CURRENT_DATE, 'buy', 'STOCKS', 'stoch-slow 5-3-3 indicates signal, please verify with other technicals and material news, ratings changes', A.close FROM public."Tech_Daily" A, public."Tech_Daily" B 
where A.ticker = B.ticker and A.date = '2021-07-08' and B.date = '2021-07-07'
and B.stochs_delta < 0 and A.stochs_delta > 0 and A.stochs_slowk < 50 

---- Stochastic & Volume BUY
SELECT A.ticker, B.stochs_delta, A.stochs_delta, B.volume, A.volume, A.volume-B.volume as volume_change, CAST((A.volume-B.volume)/B.volume as FLOAT) as volume_change_percent 
FROM public."Tech_Daily" A, public."Tech_Daily" B 
where A.ticker = B.ticker and A.date = '2021-07-08' and B.date = '2021-07-07'
and B.stochs_delta < 0 and A.stochs_delta > 0 and A.stochs_slowk < 50 

---- EMA BUY
SELECT A.ticker, CURRENT_DATE, 'buy', 'STOCKS', 'stoch-slow 5-3-3 indicates signal, please verify with other technicals and material news, ratings changes', A.close 
FROM public."Tech_Daily" A, public."Tech_Daily" B 
where A.ticker = B.ticker and A.date = '2021-06-10' and B.date = '2021-06-09'
and A.ema8 > A.ema12 and B.ema8 > B.ema12  

---- Signals 
--insert into public."Signals" (ticker, date, buy_sell, method, note) values ('ESTC', CURRENT_DATE, 'buy', 'STOCHS', 'stochs 5-3-3 turned negative to positive first time, check technicals and any events scheduled.')
insert into public."Signals" (ticker, date, buy_sell, method, note) values ('CMCSA', '2021-07-07', 'sell', 'STOCHS', 'stochs 5-3-3 turned positive to negative first time, check technicals/ resistances, all time high and any events scheduled.')
select * from public."Signals" where date='2021-07-08'

---- Stochastic Sell
SELECT A.ticker, B.stochs_delta, A.stochs_delta FROM public."Tech_Daily" A, public."Tech_Daily" B 
where A.ticker = B.ticker and A.date = '2021-07-07' and B.date = '2021-07-06'
and B.stochs_delta > 0 and A.stochs_delta < 0 and A.stochs_slowk > 70

---- Stochastic & Volume Sell
insert into public."Signals"(ticker, date, buy_sell, method, note, reco_price)
SELECT A.ticker, CURRENT_DATE, 'sell', 'STOCKS', 'stoch-slow 5-3-3 indicates signal, please verify with other technicals and material news, ratings changes', A.close FROM public."Tech_Daily" A, public."Tech_Daily" B 
where A.ticker = B.ticker and A.date = '2021-07-08' and B.date = '2021-07-07'
and B.stochs_delta > 0 and A.stochs_delta < 0 and A.stochs_slowk > 70

