from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
from turtle import Screen

snake_segments = []
game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Salman's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
screen.exitonclick()