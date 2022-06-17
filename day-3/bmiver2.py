print (" BMI 2.0   INDEX")
message="please enter your height(cm) ? "
height=float(input(message))/100
message="please enter your weight ? "
weight=float(input(message))
#you can use  if elif  else togther
bmi=round(weight/height**2,1)
if bmi<35:
    if bmi<18.5:
        message=f"your bmi is {bmi} you are underweight"
        print(message)
    elif bmi<25:
        message=f"your bmi is {bmi} you are normal weight"
        print(message)
    elif bmi<30:
        message=f"your bmi is {bmi} you are overweight"
        print(message)
    else:
        message=f"your bmi is {bmi} you are obese"
        print(message)
else:
    message=f"your bmi is {bmi} you are clinically obese"
    print(message)