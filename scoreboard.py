from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(x=-100, y=190)
        self.write(f"{self.l_score}", align= "center", font=("Courier", 80, "bold"))
        self.goto(x=100, y=190)
        self.write(f"{self.r_score}", align= "center", font=("Courier", 80, "bold"))
        self.goto(x=0, y=350)
        self.write(f" WINS!", align="center", font=("Courier", 40, "bold"))


    def refresh(self):
        self.clear()
        self.goto(x=-100, y=190)
        self.write(f"{self.l_score}", align= "center", font=("Courier", 80, "bold"))
        self.goto(x=100, y=190)
        self.write(f"{self.r_score}", align= "center", font=("Courier", 80, "bold"))


    def game_end(self):
        self.clear()
        self.goto(x=-100, y=190)
        self.write(f"{self.l_score}", align= "center", font=("Courier", 80, "bold"))
        self.goto(x=100, y=190)
        self.write(f"{self.r_score}", align= "center", font=("Courier", 80, "bold"))

        self.winner = ""
        if self.l_score > self.r_score:
            self.winner = "LEFT"
        else:
            self.winner = "RIGHT"
        self.goto(x=0, y=0)
        self.write(f"{self.winner} WINS!", align="center", font=("Courier", 40, "bold"))


