from turtle import Turtle, Screen
from random import choice

color_pantagon = ["chartreuse", "cyan", "chocolate", "coral", "blue",
                  "brown", "azure", "pink", "gold", "DogerBlue",
                  "linen", "purple", "yellow", "salmon", "tomato","wheat","peru","green"]

timmy = Turtle()
screen = Screen()
screen.bgcolor("black")
timmy.shape("turtle")
timmy.penup()
timmy.left(90)
timmy.forward(300)
timmy.left(90)
timmy.forward(100)
timmy.left(180)
timmy.pendown()
for item in range(3, 10):
    timmy.color(choice(color_pantagon))
    for _ in range(item):
        timmy.forward(200)
        timmy.right(360 / item)

screen.exitonclick()
