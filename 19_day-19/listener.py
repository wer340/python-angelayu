from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()
def move():
    timmy.forward(100)

screen.onkey(key="f",fun=move)
screen.listen()



screen.exitonclick()