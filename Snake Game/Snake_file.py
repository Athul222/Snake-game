from turtle import Turtle

#Constant variable
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
        #Creating a attribute called head so that we don't need to call index number 0 of segments
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    
    def add_segment(self, position):
        my_segment = Turtle(shape="square")
        my_segment.color("white")
        my_segment.penup()
        my_segment.goto(position) 
        self.segments.append(my_segment)
        
    def extend(self):
        #position() is a method in python which returns the position of that segment
        self.add_segment(self.segments[-1].position()) 
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    
    def move(self):    
        for seg_num in range(len(self.segments)-1, 0, -1):
            x_value = self.segments[seg_num - 1].xcor()
            y_value = self.segments[seg_num - 1].ycor()
            
            self.segments[seg_num].goto(x_value, y_value)
        self.head.forward(MOVE_DISTANCE)
    
    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
                
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)