select * from public."Daily_Data" where ticker = 'AAPL' order by date desc

select * from public."Daily_Signals"

--delete from public."Daily_Signals"

--delete from public."Weekly_Signals"

select * from public."Daily_Signals" where ticker = 'SHOP' order by date desc

select * from public."Daily_Signals" where date > '2021-07-16' order by date desc

select A.*
from public."Daily_Signals" A, public."WatchList" B
where A.ticker = B.ticker and A.date > '2021-07-16' and B.priority = 1
order by A.date desc

select * from public."Daily_Signals" A, public."WatchList" B
where A.date = '2021-07-23' and A.ticker = B.ticker and B.priority_name = 'MAIN'
order by A.date desc
