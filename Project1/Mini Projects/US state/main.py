import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('US states.csv')
all_states = data.state.to_list()
guessed_states = []
# create pop up window

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Correct',
                                    prompt='What\'s another state\'s name?').title()
    if answer_state == 'Exit':
        missing_states = []
        # ms = [state for state in all_states if state not in guessed_states] #list comprehension option
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('missed_states.csv')
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

screen.exitonclick()

