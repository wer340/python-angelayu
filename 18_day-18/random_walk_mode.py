import turtle as t
from random import choice,randint

direction=[0,90,180,270]
timmy = t.Turtle()
screen = t.Screen()
timmy.pensize(20)
timmy.speed(10)

t.colormode(255)
def color_rand():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return(r,g,b) #return tuple a data type of python  carved stone immutable
for _ in range(100):
    timmy.color(color_rand())
    timmy.forward(30)
    timmy.setheading(choice(direction))
screen.exitonclick()