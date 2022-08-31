
def turn_right():
    for item in range(1,4):
        turn_left()

 
###hurdle 
while not at_goal():
    while front_is_clear() and (not at_goal()) :
        
        print(f"front is clear = {front_is_clear()}")   
        move()
        
          
    print(f"front is clear = {front_is_clear()}")  
    while wall_in_front():
        print(f"wall in front = {wall_in_front()}")  
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    print(f"wall in front = {wall_in_front()}") 
print("you win")
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
