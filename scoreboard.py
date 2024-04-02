from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("date.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score Bord : {self.score} || High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def high_date(self):
        with open("date.txt") as file:
            score = int(file.read())
            if self.score > score:
                with open("date.txt", mode="w")as file1:
                    file1.write(str(self.score))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        self.high_date()
