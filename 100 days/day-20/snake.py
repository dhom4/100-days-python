from random import choice
from turtle import Turtle

# The Dimension of single turtle is 20x20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    """Create snake body"""
    def create_snake(self):
        for position in STARTING_POSITIONS:
            s = Turtle("square")
            s.penup()
            s.color("white")
            s.goto(position)
            self.segments.append(s)

    """make snake body move together"""
    def move(self):
        for i in range(len(self.segments)-1, 0,-1): # this loop will happen 3 times [2,1,0]
            # segments[0].color("blue")
            # segments[1].color("red")
            # segments[2].color("green")
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)















# old attempt
# s1 = Turtle(shape="square")
# s2 = Turtle(shape="square")
# s3 = Turtle(shape="square")
# s1.color("white")
# s2.color("white")
# s3.color("white")
#
# s1.setx(20)
# s2.setx(0)
# s3.setx(-20)
#
# s1.forward(100)
# s2.forward(100)
# s3.forward(100)
