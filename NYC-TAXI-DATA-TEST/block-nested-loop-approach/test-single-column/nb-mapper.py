#!/usr/bin/env python

import sys
import csv
# Setting Parameter
columnNumber = 19
count = 4
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
            print('{0} {1}\t{2}'.format(i, linelist[count], linelist2[count]))
