#11. Given a customer’s subscription start date and duration (in days), compute expiry date.
from datetime import date,timedelta
start=date.today()
duration=timedelta(days=20)
end=start+duration
print(end)
#12.Given two dates (start_date, end_date), write a function that returns the number of weekdays.
from datetime import date,timedelta,time,datetime
start_date=date(2025,12,1)
end_date=date(2025,12,7)
current=start_date
c=0
while current.weekday()<5:
    c=c+1
    current=current+timedelta(days=1)
print(c)
#13. You are given a list of attendance timestamps. Count how many fall on a Monday.
def count_monday(timestamps):
    return sum(ts.weekday()==0 for ts in timestamps)
timestamps={
    datetime(2025,12,1),
    datetime(2025,12,2),
    datetime(2025,12,3)

}
print(count_monday(timestamps))
#14. Write a function that checks if a given date is in the future, past, or today.
check=date(2025,12,1)
today=date.today()
if today==check:
    print('today')
elif today>check:
    print('past')
else:
    print('future')
# 15. Given a delivery date and expected delivery timeline (like 3 days), calculate estimated delivery date.
deliver_date=date(2025,12,1)
expected_delivery=timedelta(days=3)
estimated_delivery=deliver_date+expected_delivery
print(estimated_delivery)
#16. Calculate a user’s precise age (years, months, days) based on DOB.
user=date(2003,10,14)
current_date=date.today()
precise_age=(current_date-user).days/365
print(precise_age.__round__())
#17. Write a function that returns True if a given year is a leap year.
def leapyear(year):
    return year%4==0
print(leapyear(2004))
#18. Given a list of expiry dates, find which products expire within the next 15 days.
'''from datetime import date,timedelta,time,datetime
today=datetime.today()
list=["2025-10-1","2025-02-2025","2025-01-05"]
for d in list:
    exp=datetime.strptime(d,"%Y-%m-%d")
    if 0<=(exp-today).days<=15:
      print(d)'''
#19. Convert a list of date strings into datetime objects and sort them.
dates=["2025-12-01","2024-10-14","2025-02-01"]
dt=[datetime.strptime(d,"%Y-%m-%d") for d in dates]
print(dt.sort())