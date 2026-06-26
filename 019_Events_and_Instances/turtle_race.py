from turtle import Turtle, Screen
import random

game_on = False
colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.width(12)
    new_turtle.goto(-230, positions[i])
    new_turtle.pendown()
    all_turtles.append(new_turtle)


user_guess = screen.textinput(title="Guess", prompt="Who do you think will win the race?")

if user_guess:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_guess.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            game_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()