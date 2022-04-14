from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=7, stretch_len=1) #All turtles start 20px X 20px
        self.penup()
        self.goto(xcor, ycor)

    def up(self):
        self.new_y = self.ycor() + 30
        self.goto(self.xcor(), self.new_y)

    def down(self):
        self.new_y = self.ycor() - 30
        self.goto(self.xcor(), self.new_y)


