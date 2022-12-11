import datetime

date1 = datetime.date(year = 2022, month = 12, day = 10)
datetime1 = datetime.datetime(2022,12,13,10,55)

time1 = datetime.time(9,35)

print(datetime1.year)

def combine(date, time):
    "Construct a datetime from a given date and a given time."
    return datetime.datetime(date.year, date.month, date.day,
        time.hour, time.minute, time.second, time.microsecond)

new = combine(date= date1, time= time1)
print(f"Combinação: {new}")

dateDelta = datetime1 - new

print(dateDelta)