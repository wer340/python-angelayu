#functions outputs
print("hi")
first_name=input("whats your first name : ")
last_name=input("whats your last name : ")

def foramt_name(first_name):
    f_name=""
    for char in first_name:
        if first_name[0]==char:
           f_name +=char.capitalize()
        else:
            f_name +=char 
    print(f"{f_name} ")

foramt_name(first_name)
foramt_name(last_name)