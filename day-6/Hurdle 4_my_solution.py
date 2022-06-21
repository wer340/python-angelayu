
def turn_right():
    for item in range(1,4):
        turn_left()

def jump():

    turn_left()
    move()
    turn_right()


i=0
while not at_goal() :
  
    if wall_in_front():
        
        jump()
        i+=1  
    elif i>=1:
        move()
        turn_right()
        for item in range(0,i):
            move()
        i=0
        turn_left()
    else:
        i=0
        move()
        
   
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
