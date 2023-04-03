import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)
# df = df.dropna() # default is rows, unless set axis = 1
df1 = df.dropna(thresh=2) # row has at least 2 non na values will be kept
df2 = df.fillna(value='Fill')
df3 = df['A'].fillna(value=df['A'].mean()) # fill na value with mean

print(df3)