import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

Filesize = ["100MB","1GB","5GB","10GB","20GB"]
Normal_time = [2.08,21.29,105.47,233.43,468.89]
Cache_time = [1.66,16.31,81.56,176.45,357.27]
x = Filesize
y1 = Normal_time
y2 = Cache_time

red_patch = mpatches.Patch(color='red', label='In-Network tracking duration')
blue_patch = mpatches.Patch(color='blue', label='Without in-network tracking duration')
plt.xlabel('Message Size',fontsize=16)
plt.ylabel('Time/Sec',fontsize=16)
plt.legend(handles=[red_patch,blue_patch])
plt.plot(x,y1,'b',linewidth=4)
plt.plot(x,y2,'r',linewidth=4)
plt.yscale('log')
plt.show()
plt.savefig("temp.png")

