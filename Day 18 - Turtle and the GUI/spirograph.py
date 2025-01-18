import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.speed("fastest")
# tim.pensize(3)

angle = 0

while angle < 360:
    tim.setheading(angle)
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.circle(100)
    angle += 5


screen = Screen()
screen.exitonclick()
