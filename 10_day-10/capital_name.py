#functions outputs
print("hi")
first_name=input("whats your first name : ")
last_name=input("whats your last name : ")

def foramt_name(first_name):
    
    for char in first_name:
        if first_name[0]==char:
           first_name[0]=char.capitalize()
      
    print(f"{first_name} ")

