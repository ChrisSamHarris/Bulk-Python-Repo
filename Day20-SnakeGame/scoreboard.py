from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class ScoreBoard(Turtle): #Note not necessary to parenthesise Turtle() although we are creating a Class based on this .. Class
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.high_score = 0 #Need to calculate how to get python to open, read and write files on my local system
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High-Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
#     def game_over(self):
#         #self.clear()
#         self.goto(0, 0)
#         #self.write(f"Game Over. Your Score: {self.score}", align=ALIGNMENT, font=FONT)
#         self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

