from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, y_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(260, y_position)
        self.color(random.choice(COLORS))

    def move(self):
        self.forward(random.randint(5,20))
        self.speed(random.randint(1,3))
