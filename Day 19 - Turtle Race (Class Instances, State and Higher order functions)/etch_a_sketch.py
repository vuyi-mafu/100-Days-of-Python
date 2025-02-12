from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")


def move_forwards():
    # tim.setheading(tim.tiltangle())
    tim.forward(10)


def move_backwards():
    # tim.setheading(tim.tiltangle())
    tim.backward(10)


def move_counterclockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
