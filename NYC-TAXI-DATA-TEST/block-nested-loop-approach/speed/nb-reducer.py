#!/usr/bin/env python

import sys
from datetime import datetime, timedelta

def calculateDiffInMinutes(key1, key2):
    subKey = key1.split('T',1)
    date1 = datetime.strptime(subKey[0], "%Y-%m-%d")
    time1 = datetime.strptime(subKey[1], "%H:%M:%S")
    subKey = key2.split('T',1)
    date2 = datetime.strptime(subKey[0], "%Y-%m-%d")
    time2 = datetime.strptime(subKey[1], "%H:%M:%S")
    timeDiff = 0
    if date2 - date1 == timedelta(days=0) and time2 > time1:
        timeDiff = (time2 - time1).seconds/float(60)
    elif date2 - date1 > timedelta(days=0):
        timeDiff = (date2 - date1 -timedelta(days=1)).days * 1440 + (datetime.strptime("23:59:59", "%H:%M:%S") - time1 + time2).second/float(60);
    
    return float(timeDiff)

# Setting Parameter
k = 5
valueSize = 3
#
keySize = valueSize + 1
currentKey = None
min_value = [sys.maxsize for i in range(k)]
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    value = value.split()
    if currentKey is None or key == currentKey:
        currentKey = key
    else:
        if max(min_value)!= sys.maxsize:
            print('{0}@{1}'.format(currentKey, max(min_value)))
        
        min_value = [sys.maxsize for i in range(k)]
        currentKey = key
    key = key.split()
    manhattanDis = 0
    a = calculateDiffInMinutes(key[1], key[2])
    b = calculateDiffInMinutes(value[0], value[1])
    if len(key) == keySize and len(value) == valueSize and a != 0 and b != 0 and float(key[3])!=0 and float(value[2])!=0:
        a = float(key[3])/a
        b = float(value[2])/b
        manhattanDis = abs(a-b)
        if manhattanDis < max(min_value):
            min_value[min_value.index(max(min_value))] = manhattanDis

if currentKey is not None:
    if max(min_value)!= sys.maxsize:
            print('{0}@{1}'.format(currentKey, max(min_value)))


    
