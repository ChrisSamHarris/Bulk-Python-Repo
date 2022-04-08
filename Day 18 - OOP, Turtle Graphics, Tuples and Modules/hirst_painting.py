#==== Damien Hirst Painting Project
import turtle
from turtle import Turtle, Screen
import random
import colorgram #File > Settings > Project > preferences OR pip install colorgram


# ======= RETRIEVING COLOURS ======
# rgb_hirst_colours = []
# hirst_colours = colorgram.extract('./image.jpeg', 36)
# print(hirst_colours) # return these values as a tuple? - color properties are returned via rgb or hsl - use the for loop to filter
#
# # Shown workings on extraction ===
# for colour in hirst_colours:
#     rgb_hirst_colours.append(colour.rgb)# This wont work as the data its too diluted and messy, need to extract precisely the rgb
#     values = [Rgb(r=239, g=236, b=238),
#
# print(rgb_hirst_colours)
#
# rgb_hirst_colours = []
#
# for colour in hirst_colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_hirst_colours.append(new_colour)
#
# print(rgb_hirst_colours) # [(239, 236, 238),
#===== END ======

# Colours extracted so we don't need to complete computation each time, saving time:
extracted_colours = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 109, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (222, 137, 176), (143, 109, 57), (101, 197, 219), (206, 166, 29), (21, 58, 132), (212, 75, 91), (238, 89, 49), (141, 208, 227), (119, 192, 141), (6, 160, 87), (4, 186, 179), (106, 108, 198), (136, 29, 72), (98, 51, 37), (25, 153, 211), (228, 168, 188), (153, 213, 195), (173, 186, 221), (234, 174, 162), (30, 91, 95), (87, 47, 34), (34, 46, 84), (239, 203, 10), (33, 85, 84), (95, 27, 52)]
turtle.colormode(255)

# We can then create random colours with the following function, referencing the results in the turtle.color object
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colour = (r, g, b)
#     return random_colour


# dh_turtle.color(random.choice(extracted_colours))
# dh_turtle.dot(20)
# dh_turtle.penup()
# dh_turtle.forward(50)
# dh_turtle.color(random.choice(extracted_colours))
# dh_turtle.dot(20)

#Damien Hirst painting challenge - dots 10x10; 20 size, 50 paces = spacing
dh_turtle = Turtle()
dh_turtle.speed("fastest")

dh_turtle.penup()
dh_turtle.setheading(225)
dh_turtle.forward(300)
dh_turtle.setheading(0)

def reset():
    dh_turtle.left(90)
    dh_turtle.forward(50)
    dh_turtle.left(90)
    dh_turtle.forward(500)
    dh_turtle.right(180)

def colour_line():
    for i in range(1, 11):
        dh_turtle.dot(20, random.choice(extracted_colours))
        dh_turtle.penup()
        dh_turtle.forward(50)

for i in range(1, 11):
    colour_line()
    reset()

dh_turtle.hideturtle()

screen = Screen()
screen.exitonclick()