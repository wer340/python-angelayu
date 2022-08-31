age=int(input("enter your current age ? "));
rest_of_age=90-age
month=rest_of_age*12
week =rest_of_age *52
day=week*7
hour=day*24
message=f"you have {month} month , {week} weeks , {day} days ,{hour} hour left "
print(message)