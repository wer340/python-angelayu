from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-200, 260)
        self.write(f"level :{self.level} ", align=ALIGN, font=FONT)

    def refresh(self):
        self.clear()
        self.write(f"level :{self.level} ", align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over  ", align=ALIGN, font=FONT)
