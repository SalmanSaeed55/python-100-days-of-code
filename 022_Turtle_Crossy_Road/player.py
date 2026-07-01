from turtle import Turtle

TURTLE_DIRECTIONS = [0, 90, 180, 270]
TRAVEL_DISTANCE = 25

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.starting_position()

    def starting_position(self):
        self.setheading(TURTLE_DIRECTIONS[1])
        self.goto(0,-380)

    def move_up(self):
        if self.ycor() < 360:
            self.setheading(TURTLE_DIRECTIONS[1])
            self.forward(TRAVEL_DISTANCE)
        else:
            pass

    def move_right(self):
        if self.xcor() < 260 :
            self.setheading(TURTLE_DIRECTIONS[0])
            self.forward(TRAVEL_DISTANCE)
        else:
            pass

    def move_left(self):
        if self.xcor() > -260:
            self.setheading(TURTLE_DIRECTIONS[2])
            self.forward(TRAVEL_DISTANCE)
        else:
            pass

    def move_down(self):
        if -360 <= self.ycor():
            self.setheading(TURTLE_DIRECTIONS[3])
            self.forward(TRAVEL_DISTANCE)
        else:
            pass