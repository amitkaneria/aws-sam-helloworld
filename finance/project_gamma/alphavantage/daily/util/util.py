from dateutil.parser import parse


def is_valid_date(date):
    if date:
        try:
            parse(date)
            return True
        except:
            return False
    return False



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


def next_business_day(input_date):
    temp_day = datetime.datetime.strptime(str(input_date), '%Y-%m-%d').date() + datetime.timedelta(days=1)
    while True:
        if calendar.is_business_day(temp_day):
            break
            # print(datetime.datetime.strptime(datetime.datetime.now().date(), '%Y-%m-%d').date())
        else:
            temp_day = datetime.datetime.strptime(str(temp_day), '%Y-%m-%d').date() + datetime.timedelta(days=1)

    return temp_day


def previous_business_day(input_date):
    temp_day = datetime.datetime.strptime(str(input_date), '%Y-%m-%d').date() + datetime.timedelta(days=-1)
    while True:
        if calendar.is_business_day(temp_day):
            break
            # print(datetime.datetime.strptime(datetime.datetime.now().date(), '%Y-%m-%d').date())
        else:
            temp_day = datetime.datetime.strptime(str(temp_day), '%Y-%m-%d').date() + datetime.timedelta(days=-1)

    return temp_day


def previous_week_business_day(input_date):
    temp_day = datetime.datetime.strptime(str(input_date), '%Y-%m-%d').date() + datetime.timedelta(days=-7)
    while True:
        if calendar.is_business_day(temp_day):
            break
            # print(datetime.datetime.strptime(datetime.datetime.now().date(), '%Y-%m-%d').date())
        else:
            temp_day = datetime.datetime.strptime(str(temp_day), '%Y-%m-%d').date() + datetime.timedelta(days=-1)

    return temp_day


# business_day = '2020-12-31'
# next_business_day = next_business_day(business_day)
# print(next_business_day)

# business_day = '2020-12-31'
# previous_business_day = previous_business_day(business_day)
# print(previous_business_day)

# business_day = '2020-12-31'
# previous_week_business_day = previous_week_business_day(business_day)
# print(previous_week_business_day)

