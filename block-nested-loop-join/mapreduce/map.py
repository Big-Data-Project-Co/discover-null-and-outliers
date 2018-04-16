#!/usr/bin/env python

import sys
import string
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
# input comes from STDIN (standard input)
reader = list(reader)
for i in range(1,len(reader)):
    if len(reader[i]) != 16:
        continue
    for j in range(1,len(reader)):
        if len(reader[j]) != 16:
            continue
        if i != j:
            print('{0} {1} {2} {3} {4}\t{5} {6} {7} {8}'.format(i,reader[i][2],reader[i][6],reader[i][3],reader[i][9],reader[j][2],reader[j][6],reader[j][3],reader[j][9]))
