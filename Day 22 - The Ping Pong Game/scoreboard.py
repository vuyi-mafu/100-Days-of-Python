from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh_screen()

    def refresh_screen(self):
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.refresh_screen()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.refresh_screen()

