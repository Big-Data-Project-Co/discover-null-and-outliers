#!/usr/bin/env python
#For this test:
#Target File: standard TSV File(delimiter is '\t')
#Goal: This file works as reducer in mapreduce
# 
import sys
import numpy as np
import matplotlib.pyplot as plt

currentkey = None
lastKey = None
totalNull = 0
val = 0
xArray = np.array([])
yArray = np.array([])

def Visualization():
    global xArray
    global yArray
    global lastKey
    global val
    xArray = np.append(xArray, [float(lastKey)] )
    yArray = np.append(yArray, [float(val)])

for line in sys.stdin:
    line = line.strip()
    #Get key/value 
    key, value = line.split('\t')


    #If we are still on the same key...
    if key == currentkey:
        val = val +  int(value)
    #Otherwise, if this is a new key...
    else:
        #If this is a new key and not the first key we've seen
        if currentkey:
            #compute/output result to STDOUT (your code goes here)
            print("Column{0} has {1} null values".format(lastKey, val))
            Visualization()
            totalNull = totalNull + val
        currentkey = key
        
        #Process input for new key (your code goes here)
        val = int(value)
    lastKey = key


#Compute/output result for the last key (your code goes here)
print("Column{0} has {1} null values".format(lastKey, val))
totalNull = totalNull + val
print("ToatalNullFields: {0}".format(totalNull))
Visualization()

#Show Visualization
plt.plot(xArray, yArray, 'ro')
plt.xticks(np.arange(0, int(xArray[-1])+1, 1.0))
plt.title('null value statistics')
plt.grid(True)
plt.show()





