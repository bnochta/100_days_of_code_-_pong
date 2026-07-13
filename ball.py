from turtle import Turtle
import random

BALL_BASE_SPEED = 0.08
BALL_SPEED_CHANGE = 1.2

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_BASE_SPEED
        self.y_move = BALL_BASE_SPEED

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def ball_bounce(self):
        self.y_move *= -1

    def ball_paddle_bounce(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0,0)
        self.x_move = BALL_BASE_SPEED * random.choice([1, -1])
        self.y_move = BALL_BASE_SPEED * random.choice([1, -1])

    def increase_speed(self):
        self.x_move *= BALL_SPEED_CHANGE
        self.y_move *= BALL_SPEED_CHANGE