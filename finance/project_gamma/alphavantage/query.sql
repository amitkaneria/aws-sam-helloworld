select * from gamma.daily_data where ticker = 'SPY' order by date desc

select * from gamma.daily_data where ticker = 'QQQ' order by date desc

select * from gamma.daily_data where ticker = 'TSLA' order by date desc

select A.*
from gamma.daily_signals A, gamma.watchlist B
where A.ticker = B.ticker and A.date >='2021-08-10' and B.priority = 0
order by A.date desc

select * from gamma.daily_signals

--delete from gamma.daily_signals

--delete from gamma.weekly_signals

select * from gamma.daily_signals where ticker = 'SHOP' order by date desc

select * from gamma.daily_signals where date > '2021-07-16' order by date desc


select * from gamma.daily_signals A, gamma.watchlist B
where A.date = '2021-07-23' and A.ticker = B.ticker and B.priority_name = 'MAIN'
order by A.date desc


--delete from gamma.daily_data where ticker in ('T', 'AXP', 'CARV', 'WBA')

select * from gamma.daily_data where ticker in ('TSLA') order by date desc

select * from gamma."Weekly_Data" where ticker in ('GOOGL') order by date desc

select * from gamma.daily_data where ticker = 'SPY' order by date desc
select * from gamma.daily_data where ticker = 'SPY' order by date desc

select * from gamma.daily_signals where ticker = 'COIN' order by date desc

select * from gamma.daily_signals where date = '2021-07-07' order by date desc

--delete from gamma.watchlist where ticker in ('T', 'AXP', 'CARV', 'WBA')
select * from gamma.watchlist where ticker in ('GME', 'AMC')
select * from gamma.watchlist --where priority=3

select ticker from gamma.watchlist where daily_last_run_date < '2021-07-21' AND priority = 1 order by priority

select * from gamma.weekly_signals where date = '2021-07-23'


select * from gamma.daily_signals A, gamma.watchlist B
where A.date = '2021-07-26' and A.ticker = B.ticker and B.priority_name = 'MAIN'
order by A.date desc

select * from gamma.daily_signals A, gamma.watchlist B
where A.date = '2021-07-26' and A.ticker = B.ticker and B.priority_name = 'GROWTH'
order by A.date desc

select * from gamma.daily_signals A, gamma.watchlist B
where A.date = '2021-07-26' and A.ticker = B.ticker and B.priority_name = 'CHINA'
order by A.date desc

select * from gamma.weekly_signals A, gamma.watchlist B
where A.date = '2021-07-23' and A.ticker = B.ticker and B.priority_name = 'MAIN'
order by A.date desc

--'MAR', 'WH', 'HLT', 'HGV', 'UAL', 'DAL', ''

select distinct priority, priority_name from gamma.watchlist
order by priority

select * from gamma.watchlist-- where priority = 0

update gamma.watchlist
set priority_name = 'MEME', priority=4 where priority =9

