from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.left(90)
        self.refresh_player()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def refresh_player(self):
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)

