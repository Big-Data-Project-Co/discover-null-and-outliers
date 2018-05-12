#!/usr/bin/env python
#For this test:
#Target File: standard TSV File(delimiter is '\t')
#Goal: This file works as reducer in mapreduce
# 
import sys

currentkey = None
lastKey = None
count = 0
totalNull = 0
val = None

for line in sys.stdin:
    line = line.strip()
    #Get key/value 
    key, value = line.split('\t')


    #If we are still on the same key...
    if key == currentkey:
        val = val +  "," + str(value)
    #Otherwise, if this is a new key...
    else:
        #If this is a new key and not the first key we've seen
        if currentkey:
            #compute/output result to STDOUT (your code goes here)
            print("Row{0} has {1} null columns:{2}".format(lastKey,count,val))
            totalNull = totalNull + count
            count = 0
        currentkey = key
        
        #Process input for new key (your code goes here)
        val = str(value)
    lastKey = key
    count = count + 1


#Compute/output result for the last key (your code goes here)
print("Row{0} has {1} null columns:{2}".format(lastKey,count,val))
totalNull = totalNull + count
print("ToatalNullFields: {0}".format(totalNull))





