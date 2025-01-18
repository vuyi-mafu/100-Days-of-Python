import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

race_on = False
if user_bet:
    race_on = True

tim = Turtle(shape="turtle")
tim.color(colors[0])
tim.penup()
tim.goto(x=-220, y=-100)
turtles.append(tim)

jim = Turtle(shape="turtle")
jim.color(colors[1])
jim.penup()
jim.goto(x=-220, y=-60)
turtles.append(jim)

pim = Turtle(shape="turtle")
pim.color(colors[2])
pim.penup()
pim.goto(x=-220, y=-20)
turtles.append(pim)

kim = Turtle(shape="turtle")
kim.color(colors[3])
kim.penup()
kim.goto(x=-220, y=20)
turtles.append(kim)

lim = Turtle(shape="turtle")
lim.color(colors[4])
lim.penup()
lim.goto(x=-220, y=60)
turtles.append(lim)

him = Turtle(shape="turtle")
him.color(colors[5])
him.penup()
him.goto(x=-220, y=100)
turtles.append(him)

while race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You win!! Your {winning_color} turtle won the race!")
            else:
                print(f"You lose! The {winning_color} turtle won the race.")


screen.exitonclick()
