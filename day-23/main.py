import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.onkey(player.move, "Up")
screen.listen()
cars=[]
for num in range(0,7):
    car_manager = CarManager(-180+num*60)
    cars.append(car_manager)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for item in cars:
        item.move()

