from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.width(3)

def pen_up():
    tim.penup()


def pen_down():
    tim.pendown()

def move_forward():
    tim.forward(30)


def move_backward():
    tim.backward(30)


def turn_left():
    tim.left(15)


def turn_right():
    tim.right(15)


def clear_canvas():
    screen.resetscreen()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)

screen.onkey(key="u", fun=pen_up)
screen.onkey(key="p", fun=pen_down)

screen.onkey(key="c", fun=clear_canvas)

screen.exitonclick()