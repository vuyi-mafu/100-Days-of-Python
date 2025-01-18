import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.penup()
        self.hideturtle()

    def make_cars(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_x = random.randint(320, 340)
        random_y = random.randint(-250, 250)
        new_car.goto(random_x, random_y)
        new_car.setheading(180)
        self.all_cars.append(new_car)

    # def move_cars(self):
    #     for car in self.all_cars:
    #         self.forward(STARTING_MOVE_DISTANCE)
