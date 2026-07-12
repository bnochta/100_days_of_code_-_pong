from turtle import Turtle, Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scoreboard_l = Scoreboard((-330, 270))
scoreboard_r = Scoreboard((320, 270))



screen.onkey(paddle.paddle_up, "Up")
screen.onkey(paddle.paddle_down, "Down")

screen.onkey(paddle_2.paddle_up, "w")
screen.onkey(paddle_2.paddle_down, "s")

game_is_on = True

score_r = 0
score_l = 0

while game_is_on:
    screen.update()
    ball.ball_move()
    round_is_on = True

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.ball_bounce()

    if ball.xcor() > 325:
        if ball.distance(paddle) < 40:
            ball.ball_paddle_bounce()
    elif ball.xcor() < -325:
        if ball.distance(paddle_2) < 40:
            ball.ball_paddle_bounce()

    if ball.xcor() > 345:
        scoreboard_l.score += 1
        scoreboard_l.refresh()
        ball.hideturtle()
        ball = Ball()

    elif ball.xcor() < -370:
        scoreboard_r.score += 1
        scoreboard_r.refresh()
        ball.hideturtle()
        ball = Ball()




screen.exitonclick()

