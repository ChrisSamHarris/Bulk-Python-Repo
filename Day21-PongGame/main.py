# Pong is more complex than Snake
# 8 Goals :
# 1) Create the screen
# 2) Create and move a paddle
# 3) 2 Players = Create another Paddle
# 4) Create the ball and make it move
# 5) Detect collision with wall and bounce
# 6) Detect collision with Paddle
# 7) Detect when paddle misses
# 8) Keep each players score
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

pong = Turtle()
screen = Screen()

########
#Screen Setup
########
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1200, height=1000)
screen.listen() # Allows for user inputs
screen.tracer(0) #stops the "initiation" animation

########
#Paddle Setup
########
r_paddle = Paddle(575,0)
l_paddle = Paddle(-585, 0)

##### Paddle Controls
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

########
#Ball Setup
########
ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on == True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 480 or ball.ycor() < -480:
        ball.bounce_y()

    #Detect collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 560 or ball.distance(l_paddle) < 50 and ball.xcor() < -560:
        ball.bounce_x()
        print("paddle contact")

    #Detect when right paddle misses
    if ball.xcor() > 590:
        ball.reset_position()
        scoreboard.l_point()

    #Detect when left paddle misses
    if ball.xcor() < -590:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()