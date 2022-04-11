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
import time
from turtle import Screen, Turtle
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    snake_seg = Turtle(shape="square")
    snake_seg.color("white")
    snake_seg.penup()
    snake_seg.goto(position)
    segments.append(snake_seg)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    for seg in segments:
        seg.forward(20)


screen.exitonclick()