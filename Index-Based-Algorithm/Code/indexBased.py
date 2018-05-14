from pyspark import SparkContext,SparkConf
from csv import reader
import sys
from rtree import index
from sklearn.neighbors import NearestNeighbors
import numpy as np

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

conf = SparkConf().setAppName("pyspark")
sc = SparkContext(conf=conf)

data = sc.textFile(sys.argv[1], 1)   # read data from test file
header = data.first()
data = data.filter(lambda x: x != header)
#data = data.mapPartitions(lambda x: reader(x))  # split data
data = data.map(lambda x: x.split())
#data = data.filter(lambda x: len(x)>1)   # filter out the null value
data = data.filter(lambda x: len(x)>17)   # filter out the null value
#data = data.filter(lambda x: isfloat(x[0]) and isfloat(x[1]))
data = data.filter(lambda x: isfloat(x[0]) and isfloat(x[8]))
#data = data.map(lambda x: [float(x[0]),float(x[1])])
data = data.map(lambda x: [float(x[0]),float(x[8])])

'''
data = data.sortBy(lambda x:x[1],ascending=False)
print(data.collect())
data2 = sc.parallelize(data.take(int(0.5*data.count())))
data = data.union(data2)
print(data.collect())
'''

data.cache()
dataCollected = data.collect()
#knnobj = NearestNeighbors().fit(dataCollected)
knnobj = NearestNeighbors(algorithm = 'kd_tree').fit(dataCollected)
bc_knnobj = sc.broadcast(knnobj)
#results = data.map(lambda x: bc_knnobj.value.kneighbors(np.array(x).reshape(1,-1),n_neighbors=1))
results = data.map(lambda x: bc_knnobj.value.kneighbors(np.array(x).reshape(1,-1),n_neighbors=5))
results = results.map(lambda x: (x[1][0][0],x[0][0][4],x[1][0][4]))
#print(data.collect())
#r = results.collect()
#print(r)
data.saveAsTextFile("indexBasedData.out")
results.saveAsTextFile("indexBased.out")












'''
dataCollected = data.collect()  # return a list
#print(dataCollected)

#local

idx = index.Index(interleaved=False)
for row in range(len(dataCollected)):
    idx.insert(row,(float(dataCollected[row][0]),float(dataCollected[row][0]),float(dataCollected[row][1]),float(dataCollected[row][1])))
bc_idx = sc.broadcast(idx)

#parallel
results = data.map(lambda x: list(bc_idx.value.nearest((float(x[0]),float(x[0]),float(x[1]),float(x[1])),2)))
#data.saveAsTextFile("indexBased.out")
#collect = results.collect()
'''

'''
results = []
for row in range(len(dataCollected)):
    results.append(list(bc_idx.value.nearest((float(dataCollected[row][0]),float(dataCollected[row][0]),float(dataCollected[row][1]),float(dataCollected[row][1])),1)))
'''

'''
print(results.isEmpty())
#print(results.isEmpty())
#results.map(lambda x: x[100])
'''
