from turtle import Turtle

ALIGNMENT = "left"  # hard code
FONT = ("Courier", 14, "normal")  # hard code


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-180, 260)
        self.write(
            f"score : {self.score}          high score:{self.high_score}",
            align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_screen(self):
        self.clear()
        self.write(
            f"score : {self.score}          high score:{self.high_score}",
            align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_screen()

    # def game_over(self):
    #     self.clear()
    #     self.goto(-100, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_screen()
