from turtle import Turtle

with open("data.txt") as file:
    high_score = file.read()
    high_score = int(high_score)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.color("white")
        self.score = 0
        self.highscore = high_score
        self.scoreboard.goto(0, 280)
        # self.scoreboard.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))
        self.score_screen_refresh()

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as write_file:
                write_file.write(str(self.score))
                self.highscore = self.score
        self.score = 0
        self.score_screen_refresh()

    # def game_over(self):
    #     self.scoreboard.goto(0, 0)
    #     self.scoreboard.write(f"Game Over!", move=False, align="center", font=("Arial", 12, "normal"))

    def score_screen_refresh(self):
        # self.score += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}   High Score: {self.highscore}", move=False, align="center",
                              font=("Arial", 12, "normal"))
