"""Snake Game"""

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

BGCOLOR = "#22201A"

class Game():
    """Contains the Snake, Food, and Game status"""
    def __init__(self):
        # Don't start game on program start
        self.game_is_on = False

        # Screen setup
        self.screen = Screen()
        self.screen.setup(width=600, height=640)
        self.screen.bgcolor(BGCOLOR)
        self.screen.title("Snake Game")
        # Control when the graphics are updated
        self.screen.tracer(0)

        # Welcome Message
        self.scoreboard = Scoreboard()

        # Listen for Key Presses
        self.screen.listen()
        self.start_game()
        # self.screen.onkey(self.start_game, "g")
        self.screen.exitonclick()

    def start_game(self):
        """Changes game status to on and runs Snake Game"""
        self.game_is_on = True
        self.snake = Snake()
        self.food = Food()
        self.screen.onkey(self.snake.up,"Up")
        self.screen.onkey(self.snake.down,"Down")
        self.screen.onkey(self.snake.left,"Left")
        self.screen.onkey(self.snake.right,"Right")
        while self.game_is_on:
            # Initiate Scoreboard
            self.scoreboard.update_scoreboard()
            self.screen.update()
            time.sleep(0.075)
            self.snake.move()

            # Detect collision with food
            if self.snake.head.distance(self.food) < 20:
                self.food.refresh()
                self.snake.extend()
                self.scoreboard.increase_score()

            # Detect collision with wall
            if self.snake.head.xcor() > 290 or self.snake.head.xcor() < -300 or self.snake.head.ycor() > 285 or self.snake.head.ycor() < -310:
                self.game_is_on = False
                self.scoreboard.game_over()
                time.sleep(2.5)
                self.scoreboard.reset()
                self.snake.reset()
                self.game_is_on = True

            # Detect collision with own tail
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.game_is_on = False
                    self.scoreboard.game_over()
                    time.sleep(2.5)
                    self.scoreboard.reset()
                    self.snake.reset()
                    self.game_is_on = True

game = Game()
