from turtle import Turtle


class Obstacle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.penup()
        self.speed(3)
