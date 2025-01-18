import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.listen()
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.onkey(fun=player.move, key="Up")

game_is_on = True
#  Controls the speed of the game by controlling the screen refreshing
speed = 0.1

#  Variable for controlling car generation frequency
i = 6

while game_is_on:
    screen.update()
    time.sleep(speed)

    #  Generate a new car every 6th time
    if i % 6 == 0:
        cars.make_cars()
    i += 1

    #  Moves every car object created in car list forward by 5
    for car in cars.all_cars:
        car.forward(5)

    #  Stops every car object when it no longer on the screen
        if car.xcor() < -320:
            cars.all_cars.remove(car)

    #  Detects collision of my turtle and car objects
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False
            
    #  Detects when the turtle reaches the top of the screen and refreshes the game
    if player.ycor() == FINISH_LINE_Y:
        player.refresh_player()
        score.refresh_screen()
        speed /= 2

screen.exitonclick()
