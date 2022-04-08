import turtle
from turtle import Turtle, Screen
import random
#<keyword> <module> <keyword> <class>
# from turtle import * - Adv & DisAdv
# alias modules; 'import turtle as t'
# python packages are hosted on the internet, we plug and play using what we need:

# import heroes
# print(heroes.gen())

#color with random module:
colour_list = ["deep sky blue", "crimson", "medium orchid", "gold", "light gray", "black", "dark orange", "red",
               "spring green", "bisque"]

# python tuple (num, num, num) - similar to a list, ordered items - tuple is carved in stone, the values CANNOT be changed i.e. tuple[2] = 12 wont work
# tuple = immutable
# to use RGB 255 in turtle we need to define it with the colormode class
turtle.colormode(255)
# We can then create random colours with the following function, referencing the results in the turtle.color object
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

# Use documentation to understand how to use Modules or packages - google, stackoverflow, official documentation etc.
timmy_the_turtle = Turtle()
# If we just imported the turtle module we would hve to specify turtle.Turtle()
timmy_the_turtle.shape("turtle")

#timmy_the_turtle.color(random.choice(colour_list))
timmy_the_turtle.color(random_colour())

#====Draw a Square:
# for i in range(0, 4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

#====Draw a dashed line:
# for i in range(0, 15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#====Draw a triangle(3), square(4), pentagon(5), hexagon(6), heptagon(7), octagon(8), nonagon(9) and decagon(10) - random colour, each side = 100 length, all shapes overlaid ontop of one another and drawn out in sequence
# 360 degrees divided by the number of sides
# sides = 3
# while sides < 11:
#     angle = round(360/sides)
#     for i in range(0, sides):
#         timmy_the_turtle.right(angle)
#         timmy_the_turtle.forward(100)
#     sides += 1
#     timmy_the_turtle.color(random.choice(colour_list))  #how do we input a random colour now? - could create a list of colours and give a choice?

#====Draw a random walk - Increase the thickness of the drawing, speed up the pace of the turtle
# distance = random.randint(90, 130)
# walk_angles = [0, 90, 180, 270] # 360 excluded as this is represented with 0
# pace = 0
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed(9)
# print(distance)
#
# while pace < distance:
#     direction = random.choice(walk_angles)
# #     walk_colour = random.choice(colour_list)
#     timmy_the_turtle.color(random_colour())
#     timmy_the_turtle.setheading(direction)  #Can also use turtle.right(direction)
#     timmy_the_turtle.forward(random.randint(10, 50))
#     pace += 1
#     print(distance - pace)

#==== Draw a spirograph - Draw a number of circles with a radius of 100 in distance

# timmy_the_turtle.speed(90)
# timmy_the_turtle.pensize(4)
#
# def draw_spirograph(turn_angle):
#     for i in range(0, 360, turn_angle):
#         timmy_the_turtle.circle(300)
#         timmy_the_turtle.left(turn_angle)
#         # Can also use timmy_*.setheading()
#         timmy_the_turtle.color(random_colour())
#
# draw_spirograph(5)


screen = Screen()
screen.exitonclick()