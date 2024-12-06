import datetime

time1 = datetime.datetime.strptime("10:30:00","%H:%M:%S")
time2 = datetime.datetime.strptime("14:45:30","%H:%M:%S")
print(time2 - time1)


