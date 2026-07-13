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
scoreboard = Scoreboard()

#Right player controls
screen.onkey(paddle.paddle_up, "Up")
screen.onkey(paddle.paddle_down, "Down")

#Left player controls
screen.onkey(paddle_2.paddle_up, "w")
screen.onkey(paddle_2.paddle_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.ball_move()
    round_is_on = True

    #The ball hits the top or bottom border
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce()

    #The ball hits a paddle
    if ball.xcor() > 340:
        if ball.distance(paddle) < 50:
            ball.ball_paddle_bounce()
            ball.increase_speed()
    elif ball.xcor() < -340:
        if ball.distance(paddle_2) < 50:
            ball.ball_paddle_bounce()
            ball.increase_speed()

    #The paddle misses the ball
    if ball.xcor() > 380:
        scoreboard.l_score += 1
        scoreboard.refresh()
        ball.ball_reset()

    if ball.xcor() < -380:
        scoreboard.r_score += 1
        scoreboard.refresh()
        ball.ball_reset()

    if scoreboard.l_score > 4:
        game_is_on = False
        scoreboard.game_end()

    if scoreboard.r_score > 4:
        game_is_on = False
        scoreboard.game_end()

screen.exitonclick()

