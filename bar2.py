import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import pandas as pd

filename = '/home/nnazarov/esnet/freq2.csv'

# read data from file
df = pd.read_csv(filename, sep = ',', header = None)

# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
params = {'legend.fontsize': 20,
          'legend.handlelength': 2}
plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)
plt.rc('axes.formatter',useoffset=False)
plt.ticklabel_format(style='plain', axis='y', scilimits=(0,0))
plt.ticklabel_format(useOffset=False, style='plain')
# set height of bar

dpkt_val = df[1]

# Set position of bar on X axis
br1 = np.arange(len(dpkt_val))
plt.rcParams.update(params)
# Make the plot
plt.bar(br1, dpkt_val, color ='r', width = barWidth,
        edgecolor ='grey', label ='Subnet Frequency',hatch='*')
plt.ticklabel_format(useOffset=False, style='plain')

# Adding Xticks
plt.xlabel('Filesize', fontweight ='bold', fontsize = 20)
plt.ylabel('Time(sec)', fontweight ='bold', fontsize = 20)
#plt.xticks([r + barWidth for r in range(len(dpkt_val))],fontsize = 20)

plt.yticks(style='normal',fontsize=20)
plt.legend()
plt.grid(True, color = "grey", linewidth = "1.4")
plt.yscale('log')
ax=plt.gca()
#ax.grid(zorder=0)
ax.set_axisbelow(True)
ax.grid(color='gray', linestyle='dashed')
ax.yaxis.set_major_formatter(ScalarFormatter())
plt.show()
