"""Creates a Snake Class"""
from turtle import Turtle
STARTING_POSITIONS = [(0, -20), (-20, -20), (-40, -20)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLOR = "#30AEB0"

class Snake(Turtle):
    """Snake class"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a snake with three blocks"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds one segment to the snake at the given position"""
        new_segment = Turtle("square")
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add new segment to the end of the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves snake"""
        # Range numbers are start, stop, and step
        for seg_num in range(len(self.segments) - 1, 0 , -1):
            # Second to last segment's x and y coordinates
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Last segment move to second to last segment's position
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Moves snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        """Moves snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        """Moves snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        """Moves snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """Resets the snake to the starting position"""
        for seg in self.segments:
            # No way to deconstruct turtles, so just move them off screen
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
