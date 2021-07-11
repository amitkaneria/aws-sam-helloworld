from dateutil.parser import parse


def is_valid_date(date):
    if date:
        try:
            parse(date)
            return True
        except:
            return False
    return False
