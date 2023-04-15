import random
import turtle
from turtle import Turtle, Screen
from random import choice

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions=[-150,-100,-50,50,100,150]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
         if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")

         rand_distance = random.randint(0,10)
         turtle.forward(rand_distance)

# alpha = Turtle("turtle")
# alpha.penup()
# alpha.color(choice(colors))
# alpha.goto(x=-230, y=-100)
#
# beta = Turtle("turtle")
# beta.penup()
# beta.color(choice(colors))
# beta.goto(x=-230, y=-50)
#
# gamma = Turtle("turtle")
# gamma.penup()
# gamma.goto(x=-230, y=0)
#
# delta = Turtle("turtle")
# delta.penup()
# delta.color(choice(colors))
# delta.goto(x=-230, y=50)
#
# epsilon = Turtle("turtle")
# epsilon.penup()
# epsilon.color(choice(colors))
# epsilon.goto(x=-230, y=100)



screen.exitonclick()