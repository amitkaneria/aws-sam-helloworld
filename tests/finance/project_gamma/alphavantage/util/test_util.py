from dateutil.parser import parse
from business.calendar import Calendar
from datetime import datetime, date
from finance.project_gamma.alphavantage.util.util import last_business_day, previous_business_day, next_business_day, \
    next_week_business_day, friday_before_previous_friday, previous_friday, previous_week_business_day, date_business_day

business_day = '2020-12-31'
next_business_day = next_business_day(business_day)
print(next_business_day)

business_day = '2020-12-31'
previous_business_day = previous_business_day(business_day)
print(previous_business_day)

business_day = '2020-12-31'
previous_week_business_day = previous_week_business_day(business_day)
print(previous_week_business_day)

print(date_business_day('2021-07-18'))
print(date_business_day(date.today()))

print(last_business_day('2021-07-18'))
print(previous_business_day(last_business_day(date=None)))


print(previous_friday())
print(previous_friday(input_date='2021-07-23'))
print(previous_friday(input_date='2021-07-22'))

print(friday_before_previous_friday())
print(friday_before_previous_friday(input_date='2021-07-23'))
print(friday_before_previous_friday(input_date='2021-07-22'))

