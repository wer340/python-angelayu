
def turn_right():
    for item in range(1,4):
        turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()    
    turn_left()
#at_goal()!=true

while not at_goal() :
    jump()
    answer=at_goal()
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
