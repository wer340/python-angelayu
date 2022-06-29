

enemie=2

def my_function():
     #not advice  that modify global scop  in local scope
    print(f"your enemis is local scope : {enemie}")
    return enemie+7
enemie= my_function()
print(f"your enemis is global scope : {enemie}")