#!/usr/bin/env python

import sys

# Setting Parameter
k = 5
valueSize = 1
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
        print('{0}@{1}'.format(currentKey, max(min_value)))
        min_value = [sys.maxsize for i in range(k)]
        currentKey = key
    key = key.split()
    manhattanDis = 0
    if len(key) == keySize and len(value) == valueSize:
        for i in range(0, valueSize):
            manhattanDis += abs(int(key[i + 1]) - int(value[i]))
        if manhattanDis < max(min_value):
            min_value[min_value.index(max(min_value))] = manhattanDis

if currentKey is not None:
    print('{0}@{1}'.format(currentKey, max(min_value)))
