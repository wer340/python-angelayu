#bmi body index weight
#weight /heiht*height
#type(input(enter number))=str
weight=float(input ("please enter your weight (kg) = "))
height=float(input ("please enter your height (cm) = "))/100;

bmi=weight/height**2
print("your bmi = "+ str(int(bmi)))

  