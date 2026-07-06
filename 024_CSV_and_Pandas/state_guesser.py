from turtle import Turtle, Screen
import pandas as pd
from pandas import DataFrame, read_csv

canvas = Screen()
canvas.title("Salman's US State Game")
image = "blank_states_img.gif"
canvas.addshape(image)
turtle = Turtle()
turtle.shape(image)

state_data = DataFrame(read_csv("50_states.csv"))
state_name = state_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = canvas.textinput("Guess a state: ", "Name a state to add to the map")

    if answer_state in state_name:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = Turtle()
            t.hideturtle()
            t.penup()
            current_state_data = state_data[state_data.state == answer_state]
            t.goto(current_state_data.x.item(), current_state_data.y.item())
            t.write(answer_state, font=("Arial", 20, "bold"))
        else:
            continue
