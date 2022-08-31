

height=float(input("inter your height meter ? : "))
if height>3:
    raise ValueError("your height shouldn't be over 3 meter")
    print("wrong")
weight=float(input("inter your weight kg ? : "))
bmi=weight/height**2
bmi=round(bmi,2)
print(f"your bmi is {bmi}")
# raise TypeError("belaaa")