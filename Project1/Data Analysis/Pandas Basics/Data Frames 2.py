import numpy as np
import pandas as pd
from numpy.random import randn

# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2), hier_index,['A','B'])
df.index.names = ['Groups', 'Num']
print(df)
data1 = df.loc['G2'].loc[2]['B']
print(data1)

data2 = df.xs(1, level='Num')
print(data2)