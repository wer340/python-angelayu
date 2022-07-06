import turtle as t
from random import choice,randint

timmy = t.Turtle()
screen = t.Screen()
timmy.speed(0)

t.colormode(255)
def color_rand():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return(r,g,b) #return tuple a data type of python  carved stone immutable

for angle in range(1,90):
    timmy.color(color_rand())
    timmy.circle(120)
    timmy.left(angle*4)

screen.exitonclick()