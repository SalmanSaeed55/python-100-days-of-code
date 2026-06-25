import random
from turtle import Turtle, Screen

directions = [45, 90, 135, 180, 225, 270, 315, 360]
colours = ["black", "navy", "blue", "green", "yellow", "orange", "purple", "dark goldenrod", "medium violet red"]

tim = Turtle()
screen = Screen()
tim.pensize(15)
tim.speed(1000)

for _ in range(500):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()