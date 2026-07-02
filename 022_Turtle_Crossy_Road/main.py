from turtle import Turtle, Screen
from player import Player
from obstacles import Obstacle
import time
import random

OBSTACLE_COLORS = ["Red", "Green", "Yellow", "Blue", "Pink"]
LEFT_EDGE = -460
RIGHT_EDGE = 460
OFFSCREEN_PADDING = 40
LANE_Y_POSITIONS = list(range(-300, 261, 80))
START_X_POSITIONS = [-420, -300, -180, -60, 60, 180, 300, 420]

game_on = True


def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=800)
    screen.title("Salman's Crossy Road Game")
    screen.tracer(0)
    return screen


def create_obstacles():
    obstacles = []
    start_positions = random.sample(START_X_POSITIONS, len(LANE_Y_POSITIONS))

    for y_position, start_x in zip(LANE_Y_POSITIONS, start_positions):
        obstacle = Obstacle()
        obstacle.goto(start_x, y_position)
        obstacle.color(random.choice(OBSTACLE_COLORS))
        obstacle.setheading(0)
        obstacles.append(obstacle)

    return obstacles


def move_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle.forward(20)

        if obstacle.xcor() >= RIGHT_EDGE + OFFSCREEN_PADDING:
            obstacle.goto(LEFT_EDGE - OFFSCREEN_PADDING, obstacle.ycor())


def end_game():
    global game_on
    game_on = False
    writer.goto(0, 0)
    writer.write("Game Over", align="center", font=("Courier", 50, "bold"))
    crossy_road.onkey(None, "Up")
    crossy_road.onkey(None, "Down")
    crossy_road.onkey(None, "Left")
    crossy_road.onkey(None, "Right")
    crossy_road.update()


crossy_road = setup_screen()
player = Player()
obstacles = create_obstacles()
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("red")

crossy_road.listen()
crossy_road.onkey(player.move_up, "Up")
crossy_road.onkey(player.move_down, "Down")
crossy_road.onkey(player.move_left, "Left")
crossy_road.onkey(player.move_right, "Right")

while game_on:
    time.sleep(0.1)
    move_obstacles(obstacles)
    if player.ycor() >= 360:
        player.starting_position()

    for obstacle in obstacles:
        if player.distance(obstacle) < 20:
            end_game()
            break

    crossy_road.update()
crossy_road.exitonclick()
