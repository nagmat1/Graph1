import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

Filesize = ["100MB","1GB","5GB","10GB","20GB"]
Percent_graph = [25.27,30.51,29.31,32.29,32.42]
#Cache_time = [1.662,16.312,81.56,176.455,355.561]
x = Filesize
y1 = Percent_graph

red_patch = mpatches.Patch(color='green', label='In-Network Cache Transfer Improvement Percentile')
#blue_patch = mpatches.Patch(color='blue', label='Normal transfer duration')
plt.xlabel('File Size',fontsize=16)
plt.ylabel('Percentile',fontsize=16)
plt.legend(handles=[red_patch])
plt.plot(x,y1,'g',linewidth=4)
plt.yscale('log')
plt.xscale('log')
plt.show()
plt.savefig("temp.png")

