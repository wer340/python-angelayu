import turtle as t
from random import choice
color_rgb=[ (215, 148, 91), (214, 81, 63), (39, 22, 26), (48, 92, 140), (232, 220, 88), (143, 66, 89), (205, 71, 88), (147, 70, 60), (192, 140, 157), (123, 168, 193), (30, 19, 17), (34, 35, 49), (122, 175, 130), (33, 132, 92), (81, 166, 99), (39, 158, 194), (52, 57, 
105), (235, 220, 10)]
timmy=t.Turtle()
t.colormode(255)
screen=t.Screen()
timmy.speed()
timmy.pensize(18)
timmy.penup()
timmy.backward(200)
timmy.setheading(270)
timmy.forward(300)
timmy.setheading(0)
timmy.dot(20,choice(color_rgb))
for key in range(0,10):
    for _ in range(10):
        
        timmy.forward(50)
        timmy.dot(20,choice(color_rgb))
    timmy.setheading(90)
    timmy.forward(50)
    
    if key%2==0 and key!=9:
        timmy.dot(20,choice(color_rgb))
        timmy.setheading(180)
    elif key%2!=0 and key!=9:
        timmy.dot(20,choice(color_rgb))
        timmy.setheading(360)

screen.exitonclick()