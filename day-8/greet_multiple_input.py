import os
os.system('cls')
def greet(name,location):
   print(f"\n\n Hello {name}") 
   print(f" what is it like in { location} \n\n ******************\n") 
# now this is the default way of calling func becaause on one hand  
# ✅✅when you are typing out the code 



greet("los Angeles","scarlett") #order important

# you could use soething called keyword
#  argument instead  of just adding argument into the function call like this   
greet(location="los Angeles",name="scarlett")#order not important