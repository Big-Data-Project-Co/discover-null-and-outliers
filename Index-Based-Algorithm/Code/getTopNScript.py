import csv
import sys

c = open('/Users/KunyuYe/Desktop/finalSpark/indexBased2.out')
#c = open('/Users/KunyuYe/Desktop/indexBased.out')
reader = csv.reader(c)
reader = list(reader)
'''
print(reader[0][0].strip()[1:len(reader[0][0].strip())])
print(reader[0][1].strip())
print(reader[0][2].strip()[0:len(reader[0][2].strip())-1])
'''
max_value = [-sys.maxsize-1 for i in range(20)]
index = [-1 for i in range(20)]
for i in range(0,len(reader)):
    val = float(reader[i][1].strip())
    if val > min(max_value):
        ind = max_value.index(min(max_value))
        max_value[ind] = val
        index[ind] = i
print(index)
print(max_value)
