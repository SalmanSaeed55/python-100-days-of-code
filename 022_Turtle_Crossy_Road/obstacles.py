from turtle import Turtle


class Obstacle(Turtle):
    move_speed = 2.0

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.penup()


    def increase_speed(cls):
        cls.move_speed += 1
