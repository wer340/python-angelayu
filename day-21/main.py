from turtle import Screen
from Snake import Snake
from Food import Food
import time

screen = Screen()
snake = Snake()
food = Food()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake Game")
screen.tracer(0)  # set it zero for turn off
# three timmy  repeat a work  so use for
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# turn on animation  section Animation control

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(
            food) < 15:  # distance method measure distance between own instance with other instance inside prantess
        print("wonderful")
screen.exitonclick()
