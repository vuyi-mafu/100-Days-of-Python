import random
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)  # turns the animation off on turtle screen

snake = Snake()
food = Food()
screen_scoreboard = ScoreBoard()
screen_scoreboard.hideturtle()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
while game_on:
    screen.update()  # updates the screen with the latest animations
    time.sleep(0.1)
    snake.move()

    #  Detect collision with food

    if snake.snakes[0].distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        snake.extend()
        screen_scoreboard.score += 1
        screen_scoreboard.score_screen_refresh()

    # Detect collision with wall

    if (snake.snakes[0].xcor() > 280 or snake.snakes[0].xcor() < -300 or snake.snakes[0].ycor() > 300 or
            snake.snakes[0].ycor() < -280):
        screen_scoreboard.reset()
        snake.reset()

    #  Detect collision with tail

    for segment in snake.snakes[1:]:
        if snake.snakes[0].distance(segment) < 10:
            screen_scoreboard.reset()
            snake.reset()

screen.exitonclick()
