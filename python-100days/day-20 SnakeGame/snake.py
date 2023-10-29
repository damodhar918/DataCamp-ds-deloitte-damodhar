from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    #TODO: Create a snake body
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    #TODO: Move the snake body
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        
    #TODO: Control the snake 
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
            
        
    #TODO: Extend the snake body
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        