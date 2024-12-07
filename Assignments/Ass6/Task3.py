# Write a program to print the current date and time in the format YYYY-MM-DD HH:MM:SS.
# Create a datetime object for 1st January 2025, 12:00 PM and print it in the format Day Month, Year at HH:MM.

import datetime
currdate = datetime.datetime.now()
print(currdate)

date = datetime.datetime(2025,1,1,12,0)
print(f"{date.day}/{date.month}/{date.year} {date.hour}:{date.minute}")