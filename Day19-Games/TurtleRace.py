import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
#pop-up window
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)

#Turtle Setup
colours = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]
y_values = [-180, -120, -60, 0, 60, 120, 180]
all_turtle = []

for turtle_index in range(0, 7):
    timmeh = Turtle(shape="turtle")
    timmeh.penup()
    timmeh.color(colours[turtle_index])
    timmeh.goto(x=-235, y=y_values[turtle_index])
    all_turtle.append(timmeh)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The winning colour is {winning_colour}!")
            else:
                print(f"You Lost! The winning colour was {winning_colour}!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()