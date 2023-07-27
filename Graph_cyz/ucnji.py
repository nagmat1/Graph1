import matplotlib.pyplot as plt
import pandas as pd
import csv

colors = { '0': 'green', '1':'blue', '2':'red'}
df = pd.read_csv("graph.csv")
x = df.iloc[0:, 0]
y = df.iloc[0:, 1]
z = df.iloc[0:, 2]
renk = 'g'
print(z)

fig,ax1 = plt.subplots()
ax1.scatter(x, y, marker='.', color=colors[z])
plt.show()
