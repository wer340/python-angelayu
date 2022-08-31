
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

for item in range(1,5):
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
