from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_POSITIONS = [-390, 390]
game_on = True

screen = Screen()
screen.tracer(0)

# Screen setup
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Salman's Pong Game")

# Halfway Line Setup
line = Turtle(shape="square")
line.color("blue")
line.shapesize(stretch_wid=30, stretch_len=0.1)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

# Paddle setup
left_paddle = Paddle()
left_paddle.initial_position_paddle(PADDLE_POSITIONS[0])
right_paddle = Paddle()
right_paddle.initial_position_paddle(PADDLE_POSITIONS[1])

# Move Paddles
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 360 or ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.paddle_bounce()

    if ball.xcor() > 390:
        ball.reset_pos()
        scoreboard.update_left()

    if ball.xcor() < -390:
        ball.reset_pos()
        scoreboard.update_right()

screen.exitonclick()
