import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.cm as cm
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
print(df['hms'])

blue_patch = mpatches.Patch(color='red', label='FLOW GBPS')
plt.legend(handles=[blue_patch],prop={'size':30})
plt.xlabel('Time (start_time_ns in seconds)', fontsize=30)
plt.ylabel('Gbps', fontsize=30)
x_axis = range(len(df['hms']))
plt.scatter(x_axis, df['Gbps'],color='red')
plt.xticks([0, 10000, 20000, 30000, 40000, 50000],
           [df['hms'][0].strftime("%H:%M:%S"), df['hms'][10000].strftime("%H:%M:%S"),
            df['hms'][20000].strftime("%H:%M:%S"),
            df['hms'][30000].strftime("%H:%M:%S"), df['hms'][40000].strftime("%H:%M:%S"),
            df['hms'][50000].strftime("%H:%M:%S")])
plt.tick_params(axis='both', which='major', labelsize=20)


plt.savefig("temp.png")
plt.show()
