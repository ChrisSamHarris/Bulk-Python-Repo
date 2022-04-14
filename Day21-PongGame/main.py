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


game_is_on = True
while game_is_on == True:
    time.sleep(0)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 480 or ball.ycor() < -480:
        ball.bounce()







screen.exitonclick()