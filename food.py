"""Food Class for Snake Game"""
from turtle import Turtle
import random

COLOR = "#D7792D"

class Food(Turtle):
    """Creates a food class which inherits all of the Turtle class"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color(COLOR)
        self.speed("fastest")
        random_x = random.randint(-270, 270)
        random_y = random.randint(-290, 275)
        self.goto(random_x, random_y)

    def refresh(self):
        """Moves food to a new location"""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-290, 275)
        self.goto(random_x, random_y)
