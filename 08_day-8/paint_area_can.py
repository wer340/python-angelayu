import math
import os
os.system('cls')

#1 can  cover 5 meter square
w=float(input("enter your width area : "))
h=float(input("enter your height area : "))
def  can_for_area(w,h):
    area=w*h
    can=math.ceil(area/5)
    print(f"you \'ll need {can} for {area} meter")

can_for_area(w,h)