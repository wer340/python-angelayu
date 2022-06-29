

enemie=2

def my_function():
    enemie=0
    enemie +=5  #refrence before assignment mean user in scope not define var  and  process on var that not define
    
    print(f"your enemis is local scope : {enemie}")

my_function()
print(f"your enemis is global scope : {enemie}")