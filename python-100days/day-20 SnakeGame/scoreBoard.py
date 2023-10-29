from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = 'center'

with open(r'day-20 SnakeGame\score.txt', 'r') as file:
    SCORE_FILE = int(file.read())
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = SCORE_FILE
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(0, 290)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score : {self.high_score}", align=ALIGN, font=FONT)
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r'day-20 SnakeGame\score.txt', 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()    


