from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# when wanna collection car make object don't make inherit structure
class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        dice = random.randint(1, 7)
        if dice == 6:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_position = random.randint(-230, 250)
            new_car.goto(300, y_position)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
