
from  turtle import Turtle,Screen

timmy=Turtle()
my_screen=Screen()
timmy.shape("turtle")
timmy.color("OrangeRed3")
timmy.forward(44)
timmy.left(90)
timmy.forward(144)
screen_size=my_screen.canvheight

print(screen_size)
my_screen.bgcolor("SteelBlue")
my_screen.exitonclick()
