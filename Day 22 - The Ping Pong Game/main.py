from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

POSITIONS_1 = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]
POSITIONS_2 = [(-350, 40), (-350, 20), (-350, 0), (-350, -20), (-350, -40)]

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
game_on = True

first_paddle = Paddle()
first_paddle.create_paddle(POSITIONS_1)
second_paddle = Paddle()
second_paddle.create_paddle(POSITIONS_2)

score = Scoreboard()
ball = Ball()
speed = 0.1

screen.onkey(fun=first_paddle.move_up, key="Up")
screen.onkey(fun=first_paddle.move_down, key="Down")
screen.onkey(fun=second_paddle.move_up, key="w")
screen.onkey(fun=second_paddle.move_down, key="s")

while game_on:
    time.sleep(speed)
    screen.update()
    ball.start()

    if ball.new_ball.ycor() > 289 or ball.new_ball.ycor() < -289:
        ball.bounce_y()

    #  Detect collision with right paddle
    for seg in first_paddle.paddle:
        if ball.new_ball.distance(seg) < 20 and ball.new_ball.xcor() > 280:
            ball.bounce_x()
            speed -= 0.01

    #  Detect collision with left paddle
    for seg in second_paddle.paddle:
        if ball.new_ball.distance(seg) < 20 and ball.new_ball.xcor() < -280:
            ball.bounce_x()
            speed -= 0.01

    #  Detect when ball is out of bounds on right side
    if ball.new_ball.xcor() > 400:
        ball.new_ball.home()
        ball.x_move *= -1
        score.l_point()
        speed = 0.1

    #  Detect when ball is out of bounds on left side

    elif ball.new_ball.xcor() < -400:
        ball.new_ball.home()
        ball.x_move *= -1
        score.r_point()
        speed = 0.1

screen.exitonclick()
