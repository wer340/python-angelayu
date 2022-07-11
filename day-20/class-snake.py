from turtle import Turtle, Screen
import time

STARTIG_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()


    def create_snake(self):
        for position in STARTIG_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        # important note argument forward  be width of square that is know 20



