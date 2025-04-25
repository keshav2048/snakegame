from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score.txt") as file:
            self.highscore = file.read()
        self.highscore1 = int(self.highscore)
        self.score1 = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score {self.score1} high score: {self.highscore} ", True, align="center")

    def increase_scoreboard(self):
        self.score1 += 1
        self.update_scoreboard()
        self.goto(0, 230)

    def reset(self):
        if self.score1 > self.highscore1:
            self.highscore = self.score1
            with open("score.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score1 = 0
        self.update_scoreboard()

