from turtle import Turtle, Screen
import random

screen=Screen()
color_turtle = ["blue","purple", "black","red","green"]
                   
screen.setup(width=500,height=400)
user_bet=screen.textinput("bet turtle", "select a  color of turtle for match : blue purple black red green ? ")
timmy_objects=[]
for item in range(1,6):
    timmy=Turtle(shape="turtle")
    timmy.color(color_turtle[item-1])
    timmy.penup()
    timmy.goto(-235,-100+item*40)
    timmy_objects.append(timmy)


start_race=False
if user_bet:
    start_race=True

while start_race:
    for item in timmy_objects:
        if item.xcor()>200:
            if item.pencolor()==user_bet:
                print(f"you win color win : {item.pencolor()}")
                start_race=False
            else:
                print(f"your color[{user_bet}] lose  win color = {item.pencolor()}")
                start_race=False
        distance_rand=random.randint(0, 10)
        item.forward(distance_rand)







screen.exitonclick()