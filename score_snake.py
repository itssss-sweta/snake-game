from msilib.schema import Font
from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",18,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
       with open("file.txt") as data:
            self.highscore=int(data.read())
        self.penup()
        self.goto(x=0,y=270)
        self.color("white")
        self.hideturtle()
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score:{self.highscore}",align=ALIGNMENT,font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("file.txt",mode="w") as data:
                data.write(f"{self.highscore}")
            
        self.score=0
        self.update_score()
        

    def inc_score(self):
        self.score+=1
        self.update_score()
