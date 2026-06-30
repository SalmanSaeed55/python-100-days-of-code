from turtle import Turtle

MOVEMENT_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def initial_position_paddle(self, x_position):
        self.goto(x_position, 0)

    def paddle_up(self):
        if self.ycor() < 280:
            current = self.ycor()
            self.goto(self.xcor(), current + MOVEMENT_DISTANCE)
        else:
            pass

    def paddle_down(self):
        if -280 < self.ycor():
            current = self.ycor()
            self.goto(self.xcor(), current - MOVEMENT_DISTANCE)
        else:
            pass
