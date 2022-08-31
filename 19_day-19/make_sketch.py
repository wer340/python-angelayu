from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def w_move():
    timmy.forward(100)
def s_move():
    timmy.backward(100)
def d_move():
    timmy.setheading(timmy.heading() - 5)
    timmy.circle(120,50)
def a_move():
    timmy.setheading(timmy.heading() + 5)
    timmy.circle(120,50)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.onkey(key="w", fun=w_move)
screen.onkey(key="s",fun=s_move)
screen.onkey(key="a",fun=a_move)
screen.onkey(key="d",fun=d_move)
screen.onkey(key="c",fun=clear)
screen.listen()
screen.exitonclick()
