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
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#Screen generation and criteria
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

#Snake construction and game
snake = Snake() #Upon init the create snake function will be called
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() #This update means the screen will only update once all the segments are into place, if the update is removed, theres a lag between the segmenets moving into position
    time.sleep(0.1) # timer delays the screen refresh rate un order to make the game easier / later - Reduce this value to make the game harder
    snake.move()

    #Detect collision with food - utilising turtle class method 'distance' - https://docs.python.org/3/library/turtle.html#turtle.distance
    if snake.snake_head.distance(food) < 15:
        print("nom nom nom")
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    #Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280 :
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail. If head collides with any segment in the tail, trigger game_over
    for segment in snake.segments[1:]: #Slice the list so the snake head is excluded - Checks every segement in the tail in relation to the head
        if snake.snake_head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


#Screen termination with click
screen.exitonclick()