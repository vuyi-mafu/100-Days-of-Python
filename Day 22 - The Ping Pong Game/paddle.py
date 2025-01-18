from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = []

    def create_paddle(self, seg_list):
        for position in seg_list:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.paddle.append(segment)

    def move_up(self):

        for seg in range(len(self.paddle) - 1, 0, -1):
            new_x = self.paddle[seg - 1].xcor()
            new_y = self.paddle[seg - 1].ycor()
            self.paddle[seg].goto(new_x, new_y)

        self.paddle[0].setheading(90)
        self.paddle[0].forward(20)

    #  paddle = [seg1, seg2, seg3, seg4, seg5]
    def move_down(self):

        for seg in range(0, len(self.paddle) - 1, 1):
            new_x = self.paddle[seg + 1].xcor()
            new_y = self.paddle[seg + 1].ycor()
            self.paddle[seg].goto(new_x, new_y)

        self.paddle[len(self.paddle) - 1].setheading(270)
        self.paddle[len(self.paddle) - 1].forward(20)
