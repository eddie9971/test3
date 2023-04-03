import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {key:value for key in labels for value in my_data}

a = pd.Series(data=my_data)
print(f'a:\n{a}')
b = pd.Series(data=my_data,index=labels)
print(f'b:\n{b}')
c = pd.Series(d)
print(f'c:\n{c}')

ser1 = pd.Series([1,2,3,4], ['USA','Australia','China','England'])
ser2 = pd.Series([1,2,5,4], ['USA','Germany','Japan','Korea'])

d = ser1['USA']
print(d)