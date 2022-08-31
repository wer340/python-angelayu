import datetime as dt


date=dt.datetime.now()
print(type(date)) #object
print(f"year={date.year} and month: {date.month} ,day={date.day},hour:{date.hour}, minutes:{date.minute},second:{date.second},millisecond:{date.microsecond}")
print(f"digit day by weekday : {date.weekday()},name:{date.today().strftime('%A')}  ")
print(dir(date)) #guide

date_birthday=dt.datetime(year=1997,month=3,day=22,hour=2)
print(date_birthday)