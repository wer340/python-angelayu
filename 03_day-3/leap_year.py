print("leap year")
year=int(input("enter a year ? "))
#this year evenly divisible by 4
#not this year evenly divisible by 100
#this year evenly divisible by 400
#two way
#second way   year%4   year%100  year%400
if (year/4-int(year/4))==0:
    
    if (year/100-int(year/100))!=0:
        message=f"this {year} year is  a leap year"
        print(message)
    elif (year/400-int(year/400))==0:
        message=f"this {year} year is  a leap year"
        print(message)
    else:
         message=f"this {year} year is not a leap year"
         print(message)
    
else:
    message=f"this {year} year is not a leap year"
    print(message)
