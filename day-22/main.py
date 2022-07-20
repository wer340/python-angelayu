from turtle import Turtle, Screen
import time
from paddle import Paddle
from scoreboard import Scoeboaard
from ball import Ball

screen = Screen()
screen.tracer(0)
screen.title("pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
scoreboard = Scoeboaard()
paddle_a = Paddle((380, 0))
paddle_b = Paddle((-380, 0))
ball = Ball()

# do not open parentheses for callback function
screen.onkey(paddle_b.up, "Up")
screen.onkey(paddle_b.down, "Down")
screen.onkey(paddle_a.up, "w")
screen.onkey(paddle_a.down, "s")
screen.listen()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce() #one time this function run  if a lot of time run -1*-1=+1

screen.exitonclick()
