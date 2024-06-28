import datetime
from datetime import datetime
from time import strptime

first_date = input("Enter the first date (YYYY.MM.DD): ")
second_date = input("Enter the second date (YYYY.MM.DD): ")
date1 = datetime.strptime(first_date, "%Y %m %d")
date2 = datetime.strptime(second_date, "%Y %m %d")

difference_seconds = abs((date2 - date1).total_seconds())
x= date1.strftime("%j")
y= date2.strftime("%j")
print(abs(date1.year - date2.year)*365*24*3600 + abs( int(y)-int(x) )*24*3600)
print(f"The difference between the two dates in seconds is: {difference_seconds}")