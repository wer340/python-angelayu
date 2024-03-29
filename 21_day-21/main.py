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
    if snake.head.distance(food) < 15:
        # distance method measure distance between own instance with other instance inside prantess
        score_board.increase_score()
        snake.extend()
        food.refresh()
        print("wonderful")  # detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = False
        score_board.game_over()
    # detect collision with tail  # if any seg collision with each seg (tail) trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            game_on = False
screen.exitonclick()
