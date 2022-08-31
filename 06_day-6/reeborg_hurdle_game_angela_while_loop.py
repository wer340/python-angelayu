
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

number_hurdle=4
while number_hurdle>0:
    jump()
    number_hurdle-=1
    print(number_hurdle)

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
