from turtle import Turtle
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

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.setposition(position)
        self.segments.append(t)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        heading = self.head.heading()
        if not heading == DOWN and not heading == UP:
            self.head.setheading(UP)

    def down(self):
        heading = self.head.heading()
        if not heading == UP and not heading == DOWN:
            self.head.setheading(DOWN)

    def left(self):
        heading = self.head.heading()
        if not heading == RIGHT and not heading == LEFT:
            self.head.setheading(LEFT)

    def right(self):
        heading = self.head.heading()
        if not heading == LEFT and not heading == RIGHT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    