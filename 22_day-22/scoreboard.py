from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 28, 'normal')


class Scoeboaard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.a_score = 0
        self.b_score = 0
        self.goto(-40, 250)  # notice goto pre define write method
        self.write(f"b :{self.b_score} a :{self.a_score} ",
                   align=ALIGN, font=FONT)
        self.goto(0, 250)

    def refresh(self):
        self.clear()
        self.write(f"b :{self.b_score} a :{self.a_score} ",
                   align=ALIGN, font=FONT)
