from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("yellowgreen")
timmy.pensize(6)
timmy.penup()
timmy.backward(150)
timmy.right(90)
timmy.forward(150)
timmy.left(90)
timmy.pendown()
def dash_line():
    for _ in range(20):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def square():
    dash_line()
    timmy.left(90)


for _ in range(4):
    square()
screen.exitonclick()
