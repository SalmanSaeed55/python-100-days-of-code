from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

for i in range(4):
    timmy.forward(100)
    timmy.left(90)

timmy.penup()
timmy.left(45)
timmy.forward(100)
timmy.pendown()

for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()