import pandas as pd

data = pd.read_csv('../Files/central_park_squirrel_data.csv')
grey_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

print(grey_count,red_count,black_count)
data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_count, red_count, black_count]
}

df = pd.DataFrame(data_dict)
# df.to_csv('../Output/squirrel_count.csv')

print(data_dict)