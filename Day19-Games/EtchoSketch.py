from turtle import Turtle, Screen

timmeh = Turtle()
screen = Screen()
#Etch-o-sketch
#Requirements : W = FWD | S = BCK | A = Counter-CW | D = CW | C = Clear & reset Drawing

def move_fwd():
    timmeh.forward(10)

def move_bck():
    timmeh.back(10)

def clear():
    timmeh.clear()
    timmeh.reset()

def clock_w():
    timmeh.right(10)

def anti_clock_w():
    timmeh.left(10)

screen.listen()
screen.onkey(key="w", fun=move_fwd)
screen.onkey(key="c", fun=clear)
screen.onkey(key="d", fun=clock_w)
screen.onkey(key="a", fun=anti_clock_w)
screen.onkey(key="s", fun=move_bck)#Cant open and close () with onkey command - when we pass a function as an input, we only pass the name without the parenthesis at the end
screen.exitonclick()
