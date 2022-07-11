from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# screen.tracer(0)
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
    # if comment this line even, even though tracer(0)=off-screen frees
    # screen.update()
    # range(start=2,stop=0,step=-1) python error keyword argument like c into this function that get from c
    # for link 3 piece   third piece =second piece = first piece a new place
    # notice when see 3 squre fall in one squre in order to while loop  thats arun again !!
    for seg_num in range(len(segment) - 1, 0, -1):
        time.sleep(2)
        new_x = segment[seg_num - 1].xcor()
        new_y = segment[seg_num - 1].ycor()
        segment[seg_num].goto(new_x, new_y)
        print(
            f"x{seg_num}={segment[seg_num].xcor()} ,   y{seg_num}={segment[seg_num].ycor()}")

screen.exitonclick()
