import datetime

def convert_to_date_time(unixtime):
    return datetime.datetime.fromtimestamp(int(unixtime).strftime('%Y-%m-%d %H:%M:%S')