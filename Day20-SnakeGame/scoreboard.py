from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class ScoreBoard(Turtle): #Note not necessary to parenthesise Turtle() although we are creating a Class based on this .. Class
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        if self.score > self.high_score:
            self.score = self.high_score


#     def game_over(self):
#         #self.clear()
#         self.goto(0, 0)
#         #self.write(f"Game Over. Your Score: {self.score}", align=ALIGNMENT, font=FONT)
#         self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

