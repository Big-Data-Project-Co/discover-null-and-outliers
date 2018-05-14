#!/usr/bin/env python
#dataset: nbgq

import sys
import string
import csv

column = 23

reader = csv.reader(sys.stdin,delimiter='\t')
# input comes from STDIN (standard input)
reader = list(reader)
for i in range(1,len(reader)):
    if len(reader[i]) != column:
        continue
    for j in range(1,len(reader)):
        if len(reader[j]) != column:
            continue
        if i != j:
        	print('{0} {1} {2} {3}\t{4} {5} {6}'.format(i,reader[i][5],reader[i][13],reader[i][14],reader[j][5],reader[j][13],reader[j][14]))
