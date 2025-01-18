import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)

angle = [0, 90, 180, 270]
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]

tim.shape("turtle")
tim.color("red")
tim.pensize(10)
tim.speed(10)


def set_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def move_turtle_randomly():
    tim.pencolor(set_color())
    tim.forward(50)
    tim.setheading(random.choice(angle))


for _ in range(200):
    move_turtle_randomly()

screen = Screen()
screen.exitonclick()
