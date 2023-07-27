import pandas as pd
import numpy as np

filename = '/home/nnazarov/esnet/chaa'

# read data from file
df = pd.read_csv(filename, parse_dates=[2, 3])
df = df.sort_values(by=df.columns[11],ascending=True)
print("DF= ",df.head(500))
#print("Number of single packet flows = ",len(df[df['packets']==1]))
#print(df[(df['packets']>0) & df['packets']<2].sum())
#print("Numpy value = ",np.sum(df['packets']==1.0))

