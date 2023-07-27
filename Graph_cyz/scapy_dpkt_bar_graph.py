import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

Filesize = ["100MB", "500MB", "1GB","5GB","10GB"]
dpkt_val = [0.06, 0.33, 0.58,3.02,7.01]
scapy_val = [0.59, 2.41, 5.85, 24, 56.15]
pyshark_val = [26.26, 152.94, 261.14, 1456.02,2912.04]

x = Filesize
y1 = dpkt_val
y2 = scapy_val
y3 = pyshark_val

green_patch = mpatches.Patch(color='green', label='pyshark')
red_patch = mpatches.Patch(color='red', label='Scapy')
blue_patch = mpatches.Patch(color='blue', label='dpkt')

plt.xlabel('File Size',fontsize=16)
plt.ylabel('Logarithmic Time/Sec',fontsize=16)

plt.legend(handles=[green_patch, blue_patch, red_patch])
plt.bar(x,y1,linewidth=1,linestyle='-.')
plt.bar(x,y2,linewidth=1,linestyle='-.')
plt.bar(x,y3,linewidth=1,linestyle='-.')
plt.yscale('log')
plt.ylim([0,1000])
plt.show()
plt.savefig("temp.png")


