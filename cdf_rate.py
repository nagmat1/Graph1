# CDF Rate graph
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

filename = '/home/nnazarov/esnet/chaa'

# read data from file
df = pd.read_csv(filename, parse_dates=[2, 3])

#Sort by start_time_ns
df = df.sort_values('start_time_ns',ascending=True)

# Calculate the time difference
df['time'] = df['end_time_ns'].sub(df['start_time_ns'], axis=0)

# Calculate total-seconds of difference
df["total_seconds"] = [x.total_seconds() for x in df['time']]

# df['hms'] = pd.to_datetime(df['start_time_ns'],format="%H:%M:%S")
df['hms'] = pd.Series([x.time() for x in df['start_time_ns']])

# Calculate Rate
df['rate'] = df['packets'] / df['total_seconds']

blue_patch = mpatches.Patch(color='blue', label='Packets/duration CDF graph')
plt.legend(handles=[blue_patch])
plt.xlabel('Time (start_time_ns)', fontsize=16)
plt.ylabel('packets/duration', fontsize=16)
x_axis = range(len(df['hms']))
# CDF part
ser = df['rate'].sort_values()
ser[len(ser)] = ser.iloc[-1]
cum_dist = np.linspace(0.,1.,len(ser))
ser_cdf = pd.Series(cum_dist, index=ser)
ser_cdf.plot(drawstyle='steps')

plt.savefig("temp.png")
plt.show()
