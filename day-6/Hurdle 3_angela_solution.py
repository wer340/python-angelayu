
def turn_right():
    for item in range(1,4):
        turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()    
    turn_left()
#at_goal()!=true

while not at_goal() :
    if wall_in_front():
        jump()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
