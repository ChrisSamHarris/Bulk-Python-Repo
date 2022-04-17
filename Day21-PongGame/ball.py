from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = 5
        self.y_move = 5
        self.setheading(270)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move #X co-ordinates keep the ball moving forward
        new_y = self.ycor() + self.y_move #Y co-ordinates set the angle at which the ball moves
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 #multiply by minus one to alter between +10 and -10

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_y()
