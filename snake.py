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
        self.heat = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for sag in self.segments:
            sag.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.heat = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            seg_x = self.segments[seg_num - 1].xcor()
            seg_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(seg_x, seg_y)
        self.heat.forward(MOVE_DISTANCE)

    def up(self):
        if self.heat.heading() != DOWN:
            self.heat.setheading(UP)

    def down(self):
        if self.heat.heading() != UP:
            self.heat.setheading(DOWN)

    def right(self):
        if self.heat.heading() != LEFT:
            self.heat.setheading(RIGHT)

    def left(self):
        if self.heat.heading() != RIGHT:
            self.heat.setheading(LEFT)
