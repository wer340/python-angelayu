from turtle import Turtle
ALIGN="center"
FONT=('Arial', 28, 'normal')
class Scoeboaard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write(f"Score : ",align=ALIGN,font=FONT)
        self.goto(0,250)
