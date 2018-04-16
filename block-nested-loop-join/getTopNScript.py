import csv
import sys

c = open('/Users/KunyuYe/Desktop/milestone/final.out/part-00001')
reader = csv.reader(c,delimiter='\t')
reader = list(reader)
max_value = [-sys.maxsize-1 for i in range(5)]
index = [-1 for i in range(5)]
for i in range(0,len(reader)):
    val = int(reader[i][1])
    if val > min(max_value):
        ind = max_value.index(min(max_value))
        max_value[ind] = val
        index[ind] = i
print(index)
print(max_value)
