from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
HIGHSCORE_FILE = "high_score.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()


    def read_high_score(self):
        if os.path.exists(HIGHSCORE_FILE):
            with (open(HIGHSCORE_FILE) as file):
                contents = file.read()
                if contents.isdigit():
                    return int(contents)
        else:
            return 0


    def write_high_score(self):
        with (open(HIGHSCORE_FILE, mode="w") as file):
            file.write(f"{self.high_score}")