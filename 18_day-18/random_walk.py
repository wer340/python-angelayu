from turtle import Turtle, Screen
from random import choice,randint

color_pantagon = ["chartreuse", "cyan", "chocolate", "coral", "blue",
                  "brown", "azure", "pink", "gold",
                  "linen", "purple", "yellow", "salmon", "tomato","wheat","peru","green",]
direction=[0,90,180,270]
timmy = Turtle()
screen = Screen()
timmy.pensize(20)
timmy.speed(10)
# “fastest”: 0
# “fast”: 10
# “normal”: 6
# “slow”: 3
# “slowest”: 1
for _ in range(100):
    timmy.color(choice(color_pantagon))
    timmy.forward(30)
    timmy.setheading(choice(direction))
screen.exitonclick()