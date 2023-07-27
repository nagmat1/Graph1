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

blue_patch = mpatches.Patch(color='blue', label='Size CDF graph')
plt.legend(handles=[blue_patch])
#plt.xlabel('Time (start_time_ns)', fontsize=16)
plt.ylabel(' Size CDF ', fontsize=16)
#x_axis = range(len(df['hms']))
# CDF part
ser = df['packets'].sort_values()
ser[len(ser)] = ser.iloc[-1]
cum_dist = np.linspace(0.,1.,len(ser))
ser_cdf = pd.Series(cum_dist, index=ser)
ser_cdf.plot(drawstyle='steps')

plt.savefig("temp.png")
plt.show()
