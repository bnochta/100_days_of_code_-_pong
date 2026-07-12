from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
            super().__init__()
            self.shape("square")
            self.color("white")
            self.speed("fastest")
            self.penup()
            self.turtlesize(stretch_wid=5, stretch_len=1)
            self.goto(pos)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)