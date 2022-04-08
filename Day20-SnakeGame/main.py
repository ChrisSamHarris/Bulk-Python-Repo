#Builidng a Snake Game
# ========== Break down the problem: ==========
# 7 Steps
# Day 1:
# 1) Create a snake body
# 2) Move the snake (continuously forward
# 3) Control the snake L,R, U & D
# Day 2:
# 4) Detect collision with food
# 5) Create a scoreboard
# 6) Detect collision with wall
# 7) Detect collision with tail

from turtle import Screen, Turtle
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")


snake_seg1 = Turtle(shape="square")
snake_seg1.color("white")
snake_seg1.setx(0)

snake_seg2 = Turtle(shape="square")
snake_seg2.color("white")
snake_seg2.setx(-20)

snake_seg3 = Turtle(shape="square")
snake_seg3.color("white")
snake_seg3.setx(-40)



screen.exitonclick()