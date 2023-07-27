# Rate graph with lines, changed to scatter on step2

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

filename = '/home/nnazarov/esnet/chaa'

# read data from file
df = pd.read_csv(filename, parse_dates=[2, 3])

# Calculate the time difference
df['time'] = df['end_time_ns'].sub(df['start_time_ns'], axis=0)

# Calculate total-seconds of difference
df["total_seconds"] = [x.total_seconds() for x in df['time']]

# Calculate Rate
df['rate'] = df['packets'] / df['total_seconds']

x = df['start_time_ns']
y2 = df['rate']
blue_patch = mpatches.Patch(color='blue', label='Rate')
plt.legend(handles=[blue_patch])
plt.xlabel('Time (start_time_ns)', fontsize=20)
plt.ylabel('Rate = Gbps/total_seconds ', fontsize=20)
plt.plot(x,y2,'b',linewidth=4)

plt.savefig("temp.png")
plt.show()

