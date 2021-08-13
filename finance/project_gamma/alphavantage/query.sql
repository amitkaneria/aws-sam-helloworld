select * from public."Daily_Data" where ticker = 'SPY' order by date desc

select * from public."Daily_Data" where ticker = 'QQQ' order by date desc

select * from public."Daily_Data" where ticker = 'TSLA' order by date desc

select * from public."Daily_Signals"

--delete from public."Daily_Signals"

--delete from public."Weekly_Signals"

select * from public."Daily_Signals" where ticker = 'SHOP' order by date desc

select * from public."Daily_Signals" where date > '2021-07-16' order by date desc

select A.*
from public."Daily_Signals" A, public."WatchList" B
where A.ticker = B.ticker and A.date >='2021-08-10' and B.priority = 1
order by A.date desc

select * from public."Daily_Signals" A, public."WatchList" B
where A.date = '2021-07-23' and A.ticker = B.ticker and B.priority_name = 'MAIN'
order by A.date desc


--delete from public."Daily_Data" where ticker in ('T', 'AXP', 'CARV', 'WBA')

select * from public."Daily_Data" where ticker in ('TSLA') order by date desc

select * from public."Weekly_Data" where ticker in ('GOOGL') order by date desc

select * from public."Daily_Data" where ticker = 'SPY' order by date desc
select * from public."Daily_Data" where ticker = 'SPY' order by date desc

select * from public."Daily_Signals" where ticker = 'COIN' order by date desc

select * from public."Daily_Signals" where date = '2021-07-07' order by date desc

--delete from public."WatchList" where ticker in ('T', 'AXP', 'CARV', 'WBA')
select * from public."WatchList" where ticker in ('GME', 'AMC')
select * from public."WatchList" --where priority=3

select ticker from public."WatchList" where daily_last_run_date < '2021-07-21' AND priority = 1 order by priority

select * from public."Weekly_Signals" where date = '2021-07-23'


select * from public."Daily_Signals" A, public."WatchList" B
where A.date = '2021-07-26' and A.ticker = B.ticker and B.priority_name = 'MAIN'
order by A.date desc

select * from public."Daily_Signals" A, public."WatchList" B
where A.date = '2021-07-26' and A.ticker = B.ticker and B.priority_name = 'GROWTH'
order by A.date desc

select * from public."Daily_Signals" A, public."WatchList" B
where A.date = '2021-07-26' and A.ticker = B.ticker and B.priority_name = 'CHINA'
order by A.date desc

select * from public."Weekly_Signals" A, public."WatchList" B
where A.date = '2021-07-23' and A.ticker = B.ticker and B.priority_name = 'MAIN'
order by A.date desc

--'MAR', 'WH', 'HLT', 'HGV', 'UAL', 'DAL', ''

select distinct priority, priority_name from public."WatchList"
order by priority

select * from public."WatchList"-- where priority = 0

update public."WatchList"
set priority_name = 'MEME', priority=4 where priority =9

