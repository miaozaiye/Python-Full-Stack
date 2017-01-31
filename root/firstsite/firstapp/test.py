import datetime
import time
import calendar

print (time.localtime()[4])

print(datetime.datetime.now())


print(datetime.date.today())

print (datetime.datetime.fromtimestamp(2421077403.0))

a = datetime.date.today()
b = str(a).replace('-','/')

print (b)