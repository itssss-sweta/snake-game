from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0 )]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        self.head.color("white")
        self.tail=self.segments[-1]

        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
           

    def add_segment(self,position):
            new_segment=Turtle("square")
            new_segment.color("orange")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def reset(self):
        for segm in self.segments:
            segm.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]


    def extend(self):
        self.add_segment(self.tail.position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num - 1].xcor()
            new_y=self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def upward(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def downward(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def forward(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    

