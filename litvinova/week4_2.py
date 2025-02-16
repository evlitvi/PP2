#Python date
#1
from datetime import datetime, timedelta

currDate = datetime.today()
pastDate = currDate - timedelta(days=5)
print(f"5 days ago: {pastDate.strftime('%d.%m.%Y')}")

#2
tomorrow = currDate + timedelta(days=1)
yesterday = currDate - timedelta(days=1)
print(f"Today is {currDate.strftime('%d.%m.%Y')}, yesterday was {yesterday.strftime('%d.%m.%Y')}, tomorrow will be {tomorrow.strftime('%d.%m.%Y')}")

#3
now = datetime.today()
now_without_microsec = now.replace(microsecond=0)
print(now_without_microsec)

#4
date1Str = input("Enter 1st date in format 'dd.mm.YYYY hh.mm.ss' : ")
date2Str = input("Enter 2nd date in format 'dd.mm.YYYY hh.mm.ss' : ")

date1 = datetime.strptime(date1Str, "%d.%m.%Y %H:%M:%S")
date2 = datetime.strptime(date2Str, "%d.%m.%Y %H:%M:%S")

diffInSec = abs((date1 - date2).total_seconds())
print(f"{diffInSec} seconds")