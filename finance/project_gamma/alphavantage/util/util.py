from dateutil.parser import parse
from business.calendar import Calendar
import datetime

calendar = Calendar(
    working_days=["monday", "tuesday", "wednesday", "thursday", "friday"],
    # array items are either parseable date strings, or real datetime.date objects
    holidays=["2021-01-01", "2021-01-18", "2021-02-15", "2021-04-02", "2021-05-31", "2021-07-05", "2021-09-06", "2021-11-25", "2021-12-24",
              "2022-01-01", "2022-01-17", "2022-02-21", "2022-04-15", "2022-05-30", "2022-07-04", "2022-09-05", "2022-11-24", "2022-12-26",
              "2023-01-02", "2023-01-16", "2023-02-20", "2023-04-07", "2023-05-29", "2023-07-04", "2023-09-04", "2023-11-23", "2023-12-25"],
    extra_working_dates=[],
)

def is_valid_date(date):
    if date:
        try:
            parse(date)
            return True
        except:
            return False
    return False


def last_business_day(date=None):

    if date == None:
        date = datetime.date.today()

    if calendar.is_business_day(date):
        return date

    temp_day = datetime.datetime.strptime(str(date), '%Y-%m-%d').date() + datetime.timedelta(days=-1)
    while True:
        if calendar.is_business_day(temp_day):
            break
        else:
            temp_day = datetime.datetime.strptime(str(temp_day), '%Y-%m-%d').date() + datetime.timedelta(days=-1)

    return temp_day


def date_business_day(date):
    if calendar.is_business_day(date):
        return True
    return False


def next_business_day(input_date):
    temp_day = datetime.datetime.strptime(str(input_date), '%Y-%m-%d').date() + datetime.timedelta(days=1)
    while True:
        if calendar.is_business_day(temp_day):
            break
        else:
            temp_day = datetime.datetime.strptime(str(temp_day), '%Y-%m-%d').date() + datetime.timedelta(days=1)

    return temp_day


def next_week_business_day(input_date):
    temp_day = datetime.datetime.strptime(str(input_date), '%Y-%m-%d').date() + datetime.timedelta(days=7)
    return temp_day


def previous_business_day(input_date):
    temp_day = datetime.datetime.strptime(str(input_date), '%Y-%m-%d').date() + datetime.timedelta(days=-1)
    while True:
        if calendar.is_business_day(temp_day):
            break
        else:
            temp_day = datetime.datetime.strptime(str(temp_day), '%Y-%m-%d').date() + datetime.timedelta(days=-1)

    return temp_day


def previous_week_business_day(input_date):
    temp_day = datetime.datetime.strptime(str(input_date), '%Y-%m-%d').date() + datetime.timedelta(days=-7)
    while True:
        if calendar.is_business_day(temp_day):
            break
        else:
            temp_day = datetime.datetime.strptime(str(temp_day), '%Y-%m-%d').date() + datetime.timedelta(days=-1)

    return temp_day


def previous_friday(input_date=None):

    if input_date == None:
        current_time = datetime.date.today()
    else:
        current_time = datetime.datetime.strptime(str(input_date), '%Y-%m-%d').date()

    ## Does Last Friday fall in this week ??
    if current_time.weekday() >= 4:
        last_friday = (datetime.datetime.strptime(str(current_time), '%Y-%m-%d').date()
                       - datetime.timedelta(days=current_time.weekday() - 4))

    ## Or if Friday falls in the week before ??
    else:
        last_friday = (datetime.datetime.strptime(str(current_time), '%Y-%m-%d').date()
                       - datetime.timedelta(days=current_time.weekday())
                       + datetime.timedelta(days=4, weeks=-1))

    return last_friday


def friday_before_previous_friday(input_date=None):

    if input_date == None:
        current_time = datetime.date.today()
    else:
        current_time = datetime.datetime.strptime(str(input_date), '%Y-%m-%d').date()

    ## Does Last Friday fall in this week ??
    if current_time.weekday() >= 4:
        last_friday = (datetime.datetime.strptime(str(current_time), '%Y-%m-%d').date()
                       - datetime.timedelta(days=current_time.weekday() - 4))

    ## Or if Friday falls in the week before ??
    else:
        last_friday = (datetime.datetime.strptime(str(current_time), '%Y-%m-%d').date()
                       - datetime.timedelta(days=current_time.weekday())
                       + datetime.timedelta(days=4, weeks=-1))

    friday_before_previous_friday = last_friday + datetime.timedelta(days=-7)

    return friday_before_previous_friday

# business_day = '2020-12-31'
# next_business_day = next_business_day(business_day)
# print(next_business_day)
#
# business_day = '2020-12-31'
# previous_business_day = previous_business_day(business_day)
# print(previous_business_day)
#
# business_day = '2020-12-31'
# previous_week_business_day = previous_week_business_day(business_day)
# print(previous_week_business_day)
#
# print(date_business_day('2021-07-18'))
# print(date_business_day(datetime.date.today()))
#
# print(last_business_day('2021-07-18'))
# print(previous_business_day(last_business_day(None)))
#
#
# print(previous_friday())
# print(previous_friday(input_date='2021-07-23'))
# print(previous_friday(input_date='2021-07-22'))
#
# print(friday_before_previous_friday())
# print(friday_before_previous_friday(input_date='2021-07-23'))
# print(friday_before_previous_friday(input_date='2021-07-22'))
