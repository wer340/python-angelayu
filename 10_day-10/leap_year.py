from pickle import FALSE


print("leap year")
year=int(input("enter a year : "))
month=int(input("enter a month : "))
#this year evenly divisible by 4
#not this year evenly divisible by 100
#this year evenly divisible by 400
#two way
#second way   year%4   year%100  year%400
#in leaap year feb is 29 day
def days_in_month(year ,month):
    leap_year=False
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%4==0:
        if year%100!=0:
           leap_year=True 
        elif year%400==0:
            leap_year=True 
        else:
            leap_year=False 
    else:
        leap_year=False 
    if leap_year:
        month_days[1]=29
        
    print(f"month = {month_days[month-1]}")

days_in_month(year,month)