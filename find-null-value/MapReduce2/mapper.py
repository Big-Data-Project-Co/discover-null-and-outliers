#!/usr/bin/env python
#For this test:
#Target File: standard TSV File(delimiter is '\t')
#Goal: This file works as mapper in mapreduce
#      
import sys
import csv
firstRound = True
columnNumber = 0
count = 0
reader = csv.reader(sys.stdin, delimiter='\t')
for entry in reader:
    splitLength = len(entry)
    nullValueNumber = columnNumber - splitLength
    if firstRound == True:
        columnNumber = splitLength
        firstRound = False
    elif nullValueNumber != 0:
        print("Error: Row{0} has only {1} columns ".format(count,nullValueNumber))
    else:
        for var in range(splitLength):
            if entry[var] == "":
                print("{0}\t{1}".format(var + 1, 1))
            
    count = count + 1
    #if count > 1:
        #break