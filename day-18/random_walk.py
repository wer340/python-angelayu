from turtle import Turtle, Screen
from random import choice,randint

color_pantagon = ["chartreuse", "cyan", "chocolate", "coral", "blue",
                  "brown", "azure", "pink", "gold",
                  "linen", "purple", "yellow", "salmon", "tomato","wheat","peru","green",]
angle=[0,90,270]
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed(0)
for _ in range(200):
    move=randint(10,30)
    timmy.color(choice(color_pantagon))
    timmy.forward(move)
    timmy.left(choice(angle))
screen.exitonclick()