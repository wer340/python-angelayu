from turtle import Turtle

ALIGNMENT = "left"  # hard code
FONT = ("Courier", 24, "normal")  # hard code


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-80, 260)
        self.write(f"score : {self.score}", align=ALIGNMENT,
                   font=FONT)

        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score : {self.score}", align=ALIGNMENT,
                   font=FONT)
