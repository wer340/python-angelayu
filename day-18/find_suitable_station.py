import turtle as t
from random import choice

timmy=t.Turtle()
t.colormode(255)
screen=t.Screen()
timmy.speed()

timmy.setheading(225) #set angle    1/4 2/4 3/4 4/4  between 180-270 > 225 :)) after draw count dot *50 =8*50=400
for _ in range(10):
    
    timmy.forward(50)
    timmy.dot(20,"red")

screen.exitonclick()