import turtle
#timmy = turtle.Turtle()
#https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen
#Class
timmy = Turtle()
print(timmy)

#methods
timmy.shape("turtle")
timmy.color("DarkGreen")
timmy.forward(100)

my_screen = Screen()
#canvheight = attribute
print(my_screen.canvheight)
my_screen.exitonclick()