import datetime
import time

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

print("The epoch of this machine starts at " + time.strftime("%c", time.gmtime(0)))
print(f"The current timezone is {time.tzname[0], time.timezone}")

if time.daylight != 0:
    print("\tDaylight saving is in effect for this location")
    print("\tThe DMT timezone is " + time.tzname[1])

print("The local timezone is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
