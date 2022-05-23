from turtle import Turtle
import random
colors=random.choice(["red","blue","yellow","green"])
shapes=["circle","turtle"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(random.choice(shapes))
        self.penup()
        self.shapesize(stretch_len=0.8,stretch_wid=0.5)
        self.color(colors)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x=random.randint(-200,200)
        random_y=random.randint(-200,200)
        self.goto(random_x,random_y)

