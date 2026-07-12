from turtle import Turtle

# SCREEN_HEIGHT = 600
# SCREEN_WIDTH = 800

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 0.08
        self.y_move = 0.08

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # * (SCREEN_HEIGHT/SCREEN_WIDTH))

        self.goto(new_x, new_y)

    def ball_bounce(self):
        self.y_move *= -1

    def ball_paddle_bounce(self):
        # self.y_move *= -1
        self.x_move *= -1