import calendar
from datetime import datetime, timedelta
import random 
import time

print(calendar.month(2026,8))

now = datetime.now()
print("Current date and time:", now)

birthday = datetime(2011, 9, 2)
print("My birthday is on:", birthday)

#finding the week day
day = calendar.weekday(2011, 9, 2)
print("The weekday of my birthday is:", day)

#checking leap year
print("Is this a leap year?", calendar.isleap(2024))

#finding future date
today = datetime.now()
print("Today's date is:", today)
future_date = today+timedelta(days=7)
print("The future date is:", future_date)

print("This month calender is:", calendar.month(today.year, today.month))

def get_random_date(start_date, end_date):
    print("Printing random date between", start_date, "and", end_date)
    random_generator = random.random()
    date_format = "%Y-%m-%d"

    start_time = time.mktime(time.strptime(start_date, date_format))
    end_time = time.mktime(time.strptime(end_date, date_format))

    random_time = start_time + random_generator * (end_time - start_time)
    random_date = time.strftime(date_format, time.localtime(random_time))
    return random_date
print(get_random_date("2020-01-01", "2023-12-31"))





