import numpy as np
import pandas as pd


def times2(x):
    return x*2


df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [444, 555, 666, 444],
    'col3': ['abc', 'def', 'ghi', 'xyz']
})

print(df)
u1 = df['col2'].unique()
u2 = df['col2'].nunique()
u3 = df['col2'].value_counts()
print(u3)


# a = df['col1'].apply(times2)
# a1 = df['col2'].apply(lambda x: x*2)
# print(a1)
#
# sort1 = df.sort_values('col2')
# print(sort1)

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df1 = pd.DataFrame(data)
# df.pivot_table(values='')
