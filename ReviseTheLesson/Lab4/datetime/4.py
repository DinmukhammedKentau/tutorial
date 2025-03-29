import datetime
day1=datetime.datetime(2025,3,15,17,40,0)
day2=datetime.datetime(2025,3,15,17,40,1)
day3=day2-day1
print((day2-day1).total_seconds())