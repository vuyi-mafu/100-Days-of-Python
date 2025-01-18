import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pencolor(random.random(), random.random(), random.random())

sides = 3
while sides < 11:
    for _ in range(0, sides):
        tim.forward(100)
        tim.right(360 / sides)
    tim.pencolor(random.random(), random.random(), random.random())
    sides += 1

screen = Screen()
screen.exitonclick()
