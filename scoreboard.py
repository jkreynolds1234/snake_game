"""Scoreboard Class for Snake Game"""
from turtle import Turtle
ALIGNMENT = "center"
WELCOME_FONT = ("Courier", 18, "bold")
SCORE_FONT = ("Courier", 22, "bold")
LARGE_FONT = ("Courier", 28, "bold")
EXTRA_LARGE_FONT = ("Courier", 34, "bold")
WHITE = "#ECE3C9"
ORANGE = "#E3802A"
TEAL = "#2DC2C7"

class Scoreboard(Turtle):
    """Scoreboard Class inherits Turtle Class"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        # Welcome message & Instructions
        self.goto(0, 70)
        self.color(WHITE)
        self.write("SNAKE GAME", align=ALIGNMENT, font=EXTRA_LARGE_FONT)
        self.goto(0, 20)
        self.color(ORANGE)
        self.write("Use the arrow keys to navigate", align=ALIGNMENT, font=WELCOME_FONT)
        self.goto(0,-30)
        self.color(TEAL)
        self.write('Press "g" to start', align=ALIGNMENT, font=WELCOME_FONT)

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.clear()
        self.color(WHITE)
        self.goto(-220, 280)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=SCORE_FONT)
        if self.high_score < 10:
            self.goto(170, 280)
        elif self.high_score >= 10:
            self.goto(160, 280)
        elif self.high_score >= 100:
            self.goto(150, 280)
        self.write(f"High Score: {self.high_score}", align = ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        """Increases the score"""
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()

    def game_over(self):
        """Writes game over in the middle of the screen"""
        self.update_scoreboard()
        self.goto(0, 30)
        self.write("GAME OVER", align=ALIGNMENT, font=LARGE_FONT)
        self.goto(0, -20)
        self.write('Game will restart momentarily', align=ALIGNMENT, font=WELCOME_FONT)

    def reset(self):
        """Resets the scoreboard when the player loses"""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
