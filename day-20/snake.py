from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# three timmy  repeat a work  so use for
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment=[]
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
    segment.append(new_segment)
#turn on animation  section Animation control

game_on=True
while game_on:
    for sag in segment:
        sag.forward(20)
        screen.delay(300)







screen.exitonclick()
