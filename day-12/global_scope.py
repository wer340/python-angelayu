

enemie=2

def my_function():
    enemie+=1
    print(f"your enemis is local scope : {enemie}")

my_function()
print(f"your enemis is global scope : {enemie}")