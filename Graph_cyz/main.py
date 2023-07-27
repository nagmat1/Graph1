import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

colors = { '0': 'green', '1':'blue', '2':'red'}
df = pd.read_csv("graph.csv")
df1 = df[df.h3 > 0]
df2 = df[df.h3 == 0]
# print(df1)
# print(df["h2"])
x1 = df1.iloc[0:, 0]
y1 = df1.iloc[0:, 1]
# z = df.iloc[0:, 2]
x2 = df2.iloc[0:, 0]
y2 = df2.iloc[0:, 1]

renk = 'g'
# print(z)
#
fig,ax1 = plt.subplots()
ax1.scatter(x1, y1, marker='o', color='r')
ax1.scatter(x2, y2, marker='.', color='g')

plt.xlabel('time(where each packet was received)')
plt.ylabel('Deq_qdepth in log #of cells(cell=80bytes)')
plt.title('Deq_qdepth and deq_congest_stat Graph')
plt.legend(['Red -->deq_congest_stat != 0 , Green --> 0'],loc='lower left')
plt.grid(True)

plt.savefig('test.png')
plt.show()

# print(x)x
#
# with open('graph.csv','r') as csvfile :
#     rows = list(csv.reader(csvfile, delimiter=','))[1:]
#     for row in rows:
#         print(row[6])
#         alfa=0.8
#
#         start, end, data = int(row[6]), int(row[14]), int(row[5])
#         x = [start, end]
#         y = [data, data]
# plt.xlabel('time(milliseconds)')
# plt.ylabel('Amount of Data(bytes)')
# plt.title('VFS and EXT4 layer READ/WRITE graph')
# plt.legend(['VR = Red, ER=black, VW=blue, EW=green, vr=%d, er=%d, vw=%d,ew=%d'%(vrc,erc,vwc,ewc)],loc='lower left')
# plt.grid(True)
# plt.savefig('test.png')
