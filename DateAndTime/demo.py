import datetime

# datetime.date #-- for working with dates
# datetime.time #-- for working with time 
# datetime.datetime #-- for working with both 
# datetime.timedelta #-- represent the duration
# datetime.tzinfo #-- base class for dealing with zone 

# curr date n time 
# curr = datetime.datetime.now()
# print(curr)

# curr date only
# curr = datetime.date.today()
# print(curr)

# specific date n time 
# date = datetime.date(2024,10,16)
# print(date)
# time = datetime.time(9,30)
# print(time)

# Extracting date and time components 
# now = datetime.datetime.now()
# print("year", now.year)
# print("month", now.month)
# print("day", now.day)
# print("hour", now.hour)
# print("minute", now.minute)
# print("seconds", now.second)

# Date arithematic with  timedelta()
# Add and subtract days
today = datetime.datetime.today()
futureDate = today + datetime.timedelta(days=20)
print("20 days after today", futureDate)
pastDate = today - datetime.timedelta(days=20)
print("20 days before today", pastDate)

