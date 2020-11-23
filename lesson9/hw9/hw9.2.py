import datetime

lTime = datetime.datetime.now()
dateB = datetime.datetime(2020, 1, 1)
dateС = datetime.datetime(2020, 12, 31)
print(lTime.day, lTime.month, lTime.year)
print(dateB.day, dateB.month, dateB.year)
delta = lTime - dateB
delta2 = dateС - lTime
print(delta.days)
print(delta2.days)
