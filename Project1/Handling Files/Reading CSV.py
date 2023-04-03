# import csv

# with open('../Files/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temperature':
#             temperatures.append(row[1])
#     print(temperatures)

import pandas as pd

data = pd.read_csv('../Files/weather_data.csv')
data_dict = data.to_dict()
print(data_dict)

temp_list = data['temperature'].to_list()
print(temp_list)

print(data['temperature'].max())

# get data in row
print(data[data.Day == "Monday"])
# get the highest temperature row
print(data[data.temperature == data.temperature.max()])

monday = data[data.Day == 'Monday']
print(monday.condition)

monday_temp = int(monday.temperature)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

# Create a dataframe from scratch
data_dict1 = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [95,97,98]
}
data1 = pd.DataFrame(data_dict1)
# data1.to_csv('data.csv')
print(data1)