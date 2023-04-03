import numpy as np
import pandas as pd
from numpy.random import randn

seed = np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# a = df['W']
df['new'] = df['W'] + df['Y']
df.drop('new', axis=1, inplace=True)
# df = df.drop('E')
# print(df.shape)

# b = df.loc['A']
# print(b)
# print(df.iloc[0])

# Conditional Selection
booldf = df > 0
# print(booldf)
# print(df[booldf])
print(df[df['W']>0]) # only getting rows that are true

t = df[df['W']>0][['X','Y']]

boolser = df['W']>0
result = df[boolser]
cols = ['X','Y']
# print(result[cols])
# print(t)

# Multiple conditions -------------------------------------
# a1 = df[(df['W']>0) & (df['Y'] > 1)]
# print(a1)

a2 = df.reset_index()

newind = 'CA NY MA OR CO'.split()
df['States'] = newind
df1 = df.set_index('States')
print(df1)