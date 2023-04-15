import turtle
from turtle import Turtle, Screen

alpha = Turtle()
screen = Screen()


def move_forward():
    alpha.forward(10)


def move_back():
    alpha.back(10)


def turn_left():
    new_heading=alpha.heading()+10
    alpha.setheading(new_heading)


def turn_right():
    new_heading=alpha.heading()-10
    alpha.setheading(new_heading)


def restart():
  alpha.clear()
  alpha.penup()
  alpha.home()
  alpha.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=restart)
screen.exitonclick()
