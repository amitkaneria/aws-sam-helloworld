select * from public."Daily_Data" where ticker = 'AAPL' order by date desc

select * from public."Daily_Signals"

--delete from public."Daily_Signals"

--delete from public."Weekly_Signals"

select * from public."Daily_Signals" where ticker = 'SHOP' order by date desc

select * from public."Daily_Signals" where date > '2021-07-16' order by date desc
