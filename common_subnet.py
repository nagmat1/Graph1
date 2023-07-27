# Rate graph with lines, changed to scatter on step2

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

common = (55976,34296,34439,33346,35337,32922,33098,34279,32826,33587,13101)
union = (55976,74076,85231,92786,100133,105720,110870,115926,120204,124934,126310)
chunks = (1,2,3,4,5,6,7,8,9,10,11)

x= chunks
y1 = common
y2 =union
fig = plt.figure(figsize=(10, 10))
blue_patch = mpatches.Patch(color='blue', label='Number of Common subnets of ip_src and ip_dst')
red_patch = mpatches.Patch(color='red', label='Union of Common subsets of ip_src and ip_dst')
plt.legend(handles=[blue_patch,red_patch])
plt.xlabel('Chunks (8 million entries each)', fontsize=20)
plt.ylabel('Union of Common subsets', fontsize=20)
plt.plot(x,y1,'b',linewidth=4)
plt.plot(x,y2,'r',linewidth=4)

plt.savefig("temp.png")
plt.show()
