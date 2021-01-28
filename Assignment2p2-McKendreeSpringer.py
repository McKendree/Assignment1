import numpy as np
import matplotlib.pyplot as plt

valuesList = []
countsList = []
f = open('CollatzConjectureP1.txt')
for line in f:
    valuesList.append(line.split(',')[0])
    countsList.append(line.split(',')[1])
f.close()

valuesArr = np.array(valuesList).astype(np.int)
countsArr = np.array(countsList).astype(np.int)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.set_xlim([0,100])
ax1.set_ylim([0,np.max(countsArr[0:100])])
ax1.scatter(valuesArr[0:100], countsArr[0:100], s=3)
ax2 = fig.add_subplot(2,2,2)
ax2.set_xlim([0,1000])
ax2.set_ylim([0,np.max(countsArr[0:1000])])
ax2.scatter(valuesArr[0:1000], countsArr[0:1000], s=3)
ax3 = fig.add_subplot(2,2,3)
ax3.set_xlim([0,10000])
ax3.set_ylim([0,np.max(countsArr[0:10000])])
ax3.scatter(valuesArr[0:10000], countsArr[0:10000], s=3)

plt.show()
plt.savefig('CollatzConjectureGraph.jpg')
