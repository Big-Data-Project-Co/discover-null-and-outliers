#!/usr/bin/env python

import sys
import string

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
        min_value = [sys.maxsize for i in range(5)]
        currentkey = key
    key = key.split()
    manhattanDis = 0
    if (len(key)==5 and len(value)==4):
        for i in range(0,4):
            manhattanDis += abs(int(key[i+1])-int(value[i]))
        if manhattanDis < max(min_value):
            min_value[min_value.index(max(min_value))] = manhattanDis
        
if currentkey is not None:
    print('{0}\t{1}'.format(currentkey,max(min_value)))
