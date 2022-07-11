from turtle import Turtle, Screen
from snake_class import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake Game")
screen.tracer(0)  # set it zero for turn off
# three timmy  repeat a work  so use for

# turn on animation  section Animation control
snake = Snake()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
