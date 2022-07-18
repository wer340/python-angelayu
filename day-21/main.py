from turtle import Screen
from Snake import Snake
from Food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.setup(width=600, height=600)
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
    score_board
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(
            food) < 15:  # distance method measure distance between own instance with other instance inside prantess
        score_board.increase_score()
        food.refresh()
        print("wonderful")
screen.exitonclick()
