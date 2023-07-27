from matplotlib.pyplot import figure
from matplotlib import pyplot as plt
import numpy as np

dpkt_val = [0.06, 0.33,0.58,3.02, 7.01]
scapy_val = [0.59, 2.41,5.85,24,56.15]
pyshark_val = [26.26,152.94, 261.14,1456.02,0] #

barWidth = 0.25
br1 = np.arange(len(dpkt_val))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

params = {'legend.fontsize': 20,
          'legend.handlelength': 2}
plt.rcParams.update(params)
lw=4

fig, ax = plt.subplots(figsize =(12, 8))

ax.set_ylabel('Time(sec)', fontweight ='bold', fontsize=20)
ax.set_xlabel('Filesize', fontweight ='bold', fontsize=20)

ax.bar(br1, dpkt_val, color ='r', width = barWidth, edgecolor ='grey', label ='dpkt',hatch='*')
ax.bar(br2, scapy_val, color ='g', width = barWidth, edgecolor ='grey', label ='Scapy',hatch='//')
ax.bar(br3, pyshark_val, color ='b', width = barWidth, edgecolor ='grey', label ='pyshark',hatch='-')

plt.xticks([r + barWidth for r in range(len(dpkt_val))],
        ['100MB', '500MB', '1GB', '5GB', '10GB'],fontsize = 20)
plt.yticks(style='normal',fontsize=20)

ax.set_yscale('log')
#for y in plt.yticks():
#    print(y)
ax_ylabels = ['{}'.format(int(y)) for y in plt.yticks()[0]]
ax.set_yticklabels(ax_ylabels)
plt.legend()

# plt.yticks(np.arange(0, np.max(agent_scaling_file.iloc[:, 3] + 50), 50),  fontsize=28)
# plt.xticks(x_range[::50],  fontsize=28)
# plt.legend(fontsize=28, framealpha=0.8, handlelength=0.7, loc='upper left', bbox_to_anchor=(0, 1.25))
ax.grid(zorder=0)
# ax.ticklabel_format(useOffset=False, style='plain')
plt.show()
