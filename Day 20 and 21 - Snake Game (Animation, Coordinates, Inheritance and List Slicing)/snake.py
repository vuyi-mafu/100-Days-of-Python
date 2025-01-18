from turtle import Turtle


class Snake:

    def __init__(self):
        self.coordinates = [0, -20, -40]
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for index in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=self.coordinates[0 + index], y=0)
            self.snakes.append(new_segment)

    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.snakes[-1].xcor(), self.snakes[-1].ycor())
        self.snakes.append(new_segment)

    def move(self):

        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.snakes[0].forward(20)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()

    def up(self):
        if self.snakes[0].heading() == 0:
            self.snakes[0].left(90)
        elif self.snakes[0].heading() == 180:
            self.snakes[0].right(90)

    def down(self):
        if self.snakes[0].heading() == 0:
            self.snakes[0].right(90)
        elif self.snakes[0].heading() == 180:
            self.snakes[0].left(90)

    def left(self):
        if self.snakes[0].heading() == 90:
            self.snakes[0].left(90)
        elif self.snakes[0].heading() == 270:
            self.snakes[0].right(90)

    def right(self):
        if self.snakes[0].heading() == 90:
            self.snakes[0].right(90)
        elif self.snakes[0].heading() == 270:
            self.snakes[0].left(90)
