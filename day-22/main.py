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
    # detection vertical wall top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # one time this function run  if a lot of time run -1*-1=+1
    # detection paddle a , b
    if ball.xcor() > 340 and ball.distance(
            paddle_a) < 50 or ball.xcor() < -340 and ball.distance(
        paddle_b) < 50:
        ball.bounce_x()
    # ball pass left and right side
    if ball.xcor() > 400:
        ball.position_reset()

    if ball.xcor() < -400:
        ball.position_reset()
        # score a ++
screen.exitonclick()
