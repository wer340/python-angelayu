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
def is_leap(year ,month):
    if year%4==0:
        if year%100!=0:
           return True 
        elif year%400==0:
            return True 
        else:
            return False 
    else:
        return False 
    
        
    
def days_in_month(year,month):
    if month >12 or month < 1:
        return "invalid month"
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year,month) and month==2:
        return 29

    else:
        return month_days[month-1]

print(days_in_month(year,month))