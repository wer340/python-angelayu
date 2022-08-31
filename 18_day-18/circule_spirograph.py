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
def draw_spirograph(size_gap):
    for _ in range(int(360/size_gap)):
        timmy.color(color_rand())
        timmy.circle(120)
        timmy.setheading(timmy.heading()+size_gap)

draw_spirograph(3)
screen.exitonclick()