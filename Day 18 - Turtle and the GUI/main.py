import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
color_list = [(237, 224, 80), (205, 4, 73), (236, 50, 130),
              (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63),
              (29, 189, 111), (22, 107, 174),
              (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160),
              (7, 49, 26), (34, 136, 72),
              (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]
tim = Turtle()
tim.hideturtle()
my_screen = Screen()
tim.teleport(-220, -200)
rows = 0
axis = 0
while rows < 10:
    axis += 50
    #  Writes 10dots on a single row
    for _ in range(0, 10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    rows += 1
    #  Moves turtle to new row on the y-axis
    tim.teleport(-220, -200 + axis)
my_screen.exitonclick()
