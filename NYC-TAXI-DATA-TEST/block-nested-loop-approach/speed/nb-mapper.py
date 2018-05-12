#!/usr/bin/env python

import sys
import csv
# Setting Parameter
columnNumber = 19
dropoffTimeCol = 2
pickupTimeCol = 3
dis = 8
#
reader = csv.reader(sys.stdin)
# input comes from standard input
reader = list(reader)
for i in range(1, len(reader)):
    linelist = reader[i][0].split()
    #if len(reader[i]) != columnNumber:
        #continue
    for j in range(1, len(reader)):
        #if len(reader[j]) != columnNumber:
            #continue
        linelist2 = reader[j][0].split()
        if i != j:
            print('{0} {1} {2} {3}\t{4} {5} {6}'.format(i, linelist[pickupTimeCol], linelist[dropoffTimeCol], linelist[dis], linelist2[pickupTimeCol], linelist2[dropoffTimeCol], linelist2[dis]))
