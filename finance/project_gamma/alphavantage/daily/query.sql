---- Tech daily
SELECT * FROM public."Tech_Daily"
where ticker = 'CLDR' --and date > '2021-01-01'
ORDER BY ticker ASC, date desc

---- Stochastic Buy
insert into public."Signals"(ticker, date, buy_sell, method, note, reco_price)
SELECT A.ticker, B.date, 'buy', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicates signal, please verify with other technicals and material news, ratings changes', B.close FROM public."Tech_Daily" A, public."Tech_Daily" B
where A.ticker = B.ticker and A.date = '2021-07-13'  and B.date = '2021-07-14'
--and A.stochs_delta < 0 and B.stochs_delta > 0  and A.stochs_slowk < 40
and ((A.stochs_delta < 0 and B.stochs_delta > 0  and A.stochs_slowk < 65) OR ((B.stochs_delta - A.stochs_delta) > 10))

---- EMA BUY
--insert into public."Signals"(ticker, date, buy_sell, method, note, reco_price)
SELECT A.ticker, A.date, 'buy', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', A.close
FROM public."Tech_Daily" A, public."Tech_Daily" B
where A.ticker = B.ticker and B.date = '2021-07-13' and A.date = '2021-07-14'
and B.ema8 < B.ema12  and A.ema8 > A.ema12 --and A.ticker = 'OKTA'
-- DONE from 06/01/2021 -- until 07/09

---- RSI Buy -- OVERSOLD
--insert into public."Signals"(ticker, date, buy_sell, method, note, reco_price)
SELECT A.ticker, B.date, 'buy', 'RSI_LOW', 'RSI oversold, check other technicals', A.close FROM public."Tech_Daily" A, public."Tech_Daily" B
where A.ticker = B.ticker and A.date = '2021-06-18'  and B.date = '2021-06-21'
and A.stochs_delta < 0 and B.stochs_delta > 0  and A.rsi < 30

-- FIND ALL stocks with RSI OVERSOLD (less than 30)
--insert into public."Signals"(ticker, date, buy_sell, method, note, reco_price)
SELECT A.ticker, A.date, 'buy', 'RSI_LOW', A.rsi || ', RSI oversold, check other technicals', A.close
from public."Tech_Daily" A
where A.rsi < 30 and A.date = '2021-07-14'
ORDER BY date desc, ticker ASC

---- Signals
--insert into public."Signals" (ticker, date, buy_sell, method, note) values ('ESTC', CURRENT_DATE, 'buy', 'STOCHS', 'stochs 5-3-3 turned negative to positive first time, check technicals and any events scheduled.')
insert into public."Signals" (ticker, date, buy_sell, method, note) values ('CMCSA', '2021-07-07', 'sell', 'STOCHS', 'stochs 5-3-3 turned positive to negative first time, check technicals/ resistances, all time high and any events scheduled.')
select * from public."Signals" where date>'2021-07-09' order by ticker, date
--delete from public."Signals" where date='2021-07-09'
select * from public."Signals" where method = 'EMA_8_12'
select * from public."Signals" where ticker = 'AMZN' order by date


---- Stochastic & Volume Sell
insert into public."Signals"(ticker, date, buy_sell, method, note, reco_price)
SELECT A.ticker, B.date, 'sell', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicates signal, please verify with other technicals and material news, ratings changes', B.close FROM public."Tech_Daily" A, public."Tech_Daily" B
where A.ticker = B.ticker and A.date = '2021-07-13' and B.date = '2021-07-14'
and A.stochs_delta > 0 and B.stochs_delta < 0  and A.stochs_slowk > 70
-- DONE from 06/01/2021 -- until 07/09

SELECT A.ticker, B.date, 'sell', 'STOCH_SLOW', 'stoch-slow 5-3-3 indicates signal, please verify with other technicals and material news, ratings changes', B.close FROM public."Tech_Daily" A, public."Tech_Daily" B
where A.ticker = B.ticker and A.date = '2021-07-13' and B.date = '2021-07-14'
--and A.stochs_delta > 0 and B.stochs_delta < 0  and A.stochs_slowk > 70
and ((A.stochs_delta > 0 and B.stochs_delta < 0  and A.stochs_slowk > 25) OR ((A.stochs_delta - B.stochs_delta) > 10))

---- EMA SELL
insert into public."Signals"(ticker, date, buy_sell, method, note, reco_price)
SELECT A.ticker, B.date, 'sell', 'EMA_8_12', 'EMA 8 crossing EMA upside indicates buy signal, please verify with other technicals and material news, ratings changes', A.close
FROM public."Tech_Daily" A, public."Tech_Daily" B
where A.ticker = B.ticker and A.date = '2021-07-13' and B.date = '2021-07-14'
and A.ema8 > A.ema12 and B.ema8 < B.ema12   --and A.ticker = 'OKTA'
-- DONE from 06/01/2021 -- until 07/09

