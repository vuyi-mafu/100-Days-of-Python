from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.new_ball = Turtle()
        self.new_ball.shape("circle")
        self.new_ball.color("white")
        self.new_ball.penup()
        self.x_move = 10
        self.y_move = 10

    def start(self):
        # self.new_ball.setheading(50)
        # self.new_ball.forward(0.5)
        self.new_ball.speed(0)
        new_x = self.new_ball.xcor() + self.x_move
        new_y = self.new_ball.ycor() + self.y_move
        self.new_ball.goto(new_x, new_y)

    def bounce_y(self):
        # if self.new_ball.ycor() > 0:
        # self.new_ball.setheading(315)
        # self.new_ball.forward(0.5)

        self.y_move *= -1

        # elif self.new_ball.ycor() < 0:
        #     self.new_ball.setheading(heading)
        #     self.new_ball.forward(0.5)
    def bounce_x(self):
        self.x_move *= -1
