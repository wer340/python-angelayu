from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
# three timmy  repeat a work  so use for
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment=[]
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segment.append(new_segment)
#turn on animation  section Animation control

game_on=True
while game_on:
    screen.update()  # if comment this line even even though traacer(0)=off  screen freez
    time.sleep(0.1)
    for sag in segment:
        sag.forward(20)
    segment[0].left(90)






screen.exitonclick()
