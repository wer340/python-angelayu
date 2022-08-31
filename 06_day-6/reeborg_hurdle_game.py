
def turn_simple():
    move()
    turn_left()
def turn_complicated():
    move()
    for item in range(1,4):
      turn_left()
def turn_mix(): 
    for item in range(1,5):
     turn_simple()
     turn_complicated() 
     turn_complicated()
     turn_simple()

turn_mix()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
