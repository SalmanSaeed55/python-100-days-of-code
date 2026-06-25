import turtle

import colorgram
from turtle import Turtle, Screen
import random

turtle.colormode(255)

colors = colorgram.extract("reference_painting.png", 20)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

"""
10x10 rows of spots
dot size = 20
spaced = 50
"""

painter = Turtle()
screen = Screen()

painter.penup()
painter.setheading(225)
painter.forward(250)
painter.setheading(0)

for i in range(10):
    for i in range(10):
        painter.pendown()
        painter.dot(20, random.choice(rgb_colors))
        painter.penup()
        painter.forward(50)

    painter.setheading(90)
    painter.forward(50)
    painter.setheading(180)
    painter.forward(500)
    painter.setheading(0)

screen.exitonclick()