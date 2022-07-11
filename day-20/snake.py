from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake Game")
screen.tracer(0)  # set it zero for turn off
# three timmy  repeat a work  so use for
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment = []

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segment.append(new_segment)
# turn on animation  section Animation control

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segment) - 1, 0, -1):
        new_x = segment[seg_num - 1].xcor()
        new_y = segment[seg_num - 1].ycor()
        segment[seg_num].goto(new_x, new_y)
    # important note argument forward  be width of square that is know 20
    segment[0].forward(20)
    segment[0].left(90)

screen.exitonclick()
