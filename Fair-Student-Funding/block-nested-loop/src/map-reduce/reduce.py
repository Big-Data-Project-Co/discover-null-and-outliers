#!/usr/bin/env python
#dataset: nbgq

import sys
import string

KEY = 4
VAL = 3

currentkey = None
min_value = [sys.maxsize for i in range(5)]
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t',1)
    value = value.split()
    if currentkey == None or key == currentkey:
        currentkey = key
    else:
        print('{0}\t{1}'.format(currentkey,max(min_value)))
        min_value = [sys.maxsize for i in range(KEY)]
        currentkey = key
    key = key.split()
    manhattanDis = 0
    if (len(key)==KEY and len(value)==VAL):
        for i in range(0,KEY-1):
            manhattanDis += abs(float(key[i+1])-float(value[i]))
        if manhattanDis < max(min_value):
            min_value[min_value.index(max(min_value))] = manhattanDis
        
if currentkey is not None:
    print('{0}\t{1}'.format(currentkey,max(min_value)))
