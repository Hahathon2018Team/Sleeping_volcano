import datetime

def convert_to_date_time(unixtime):
    return datetime.datetime.fromtimestamp(int(unixtime).strftime('%Y-%m-%d %H:%M:%S')

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1