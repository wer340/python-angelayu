import turtle as t
from random import choice
color_rgb=[ (215, 148, 91), (214, 81, 63), (39, 22, 26), (48, 92, 140), (232, 220, 88), (143, 66, 89), (205, 71, 88), (147, 70, 60), (192, 140, 157), (123, 168, 193), (30, 19, 17), (34, 35, 49), (122, 175, 130), (33, 132, 92), (81, 166, 99), (39, 158, 194), (52, 57, 
105), (235, 220, 10)]
timmy=t.Turtle()
timmy.hideturtle()
t.colormode(255)
screen=t.Screen()
timmy.speed(0)
timmy.penup()
timmy.setheading(225)
timmy.forward(400)
timmy.setheading(0)


for counter in range(1,101): # 0 %10==0 true  bug
    timmy.dot(20,choice(color_rgb))
    timmy.forward(50)
    if counter % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.exitonclick()