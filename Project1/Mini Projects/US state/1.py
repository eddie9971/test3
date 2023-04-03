import pandas as pd

data = pd.read_csv('US states.csv')
all_states = data.state.to_list()
print(all_states)
answer_state = input('').title()
state_data = data[data.state == answer_state]
print(state_data.x)