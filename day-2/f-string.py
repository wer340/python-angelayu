#f-string diffrent data type   front string
#realy painful every  time  +  strr +  a lot convert 
#print("your bmi = "+ str(int(bmi)))
weight=float(input ("please enter your weight (kg) = "))
height=float(input ("please enter your height (cm) = "))/100;

bmi=weight/height**2
bmi=round(bmi,2)
print(f"your bmi is {bmi}")
