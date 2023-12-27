### Dates ###

from datetime import datetime 

now = datetime.now()

print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.second)


timestamp = now.timestamp()
print(timestamp)


year_2024 = datetime(2024,1,1,00,30,5)

def print_date(date):
    print(date.day)
    print(date.month)
    print(date.year)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(year_2024)


from datetime import time


current_time = time(hour=19,minute=44,second=33)

print("###################")
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date


current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023,11,27)

print(current_date.year)
print(current_date.month)
print(current_date.day)



current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.year)
print(current_date.month)
print(current_date.day)

print(year_2024 - now)

from datetime import timedelta

start_timedelta = timedelta(200,10,100, weeks=10)
end_timedelta = timedelta(300,10,100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
