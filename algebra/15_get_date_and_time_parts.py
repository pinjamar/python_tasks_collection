from datetime import datetime, timedelta

def get_date_and_time_parts(datetime_string):
    datetime_object = datetime.strptime(datetime_string, "%m/%d/%Y %H:%M")
    year = datetime_object.year
    month = datetime_object.month
    day = datetime_object.day
    hour = datetime_object.hour
    minute = datetime_object.minute

    return year, month, day, hour, minute