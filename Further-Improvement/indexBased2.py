from pyspark import SparkContext,SparkConf
from csv import reader
import sys
from rtree import index
from sklearn.neighbors import NearestNeighbors
import numpy as np

from math import sqrt
from operator import add
from pyspark.mllib.clustering import KMeans, KMeansModel

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def addclustercols(x):
    point = x 
    center = clusters.centers[0]
    mindist = sqrt(sum([y**2 for y in (point - center)]))
    cl = 0
    for i in range(1,len(clusters.centers)):
        center = clusters.centers[i]
        distance = sqrt(sum([y**2 for y in (point - center)])) 
        if distance < mindist:
            cl = i
            mindist = distance
    clcenter = clusters.centers[cl]
    return np.array([point[0],point[1],cl,float(clcenter[0]),float(clcenter[1]),float(mindist)])


conf = SparkConf().setAppName("pyspark")
sc = SparkContext(conf=conf)

data = sc.textFile(sys.argv[1], 1)   # read data from test file
header = data.first()
data = data.filter(lambda x: x != header)
#data = data.mapPartitions(lambda x: reader(x))  # split data
data = data.map(lambda x: x.split())
#data = data.filter(lambda x: len(x)>1)   # filter out the null value
data = data.filter(lambda x: len(x)>17)   # filter out the null value

data = data.filter(lambda x: isfloat(x[0]) and isfloat(x[8]))

#print(len(data.collect()))


data = data.map(lambda x: np.array([float(x[0]),float(x[8])]))
clusters = KMeans.train(data, 10, maxIterations=10,initializationMode="randon")
res = data.map(lambda x: addclustercols(x))
print(res.map(lambda y: (y[2],1)).reduceByKey(add).collect())
for i in range(len(clusters.centers)):
    print(str(i)+"     "+str(clusters.centers[i]))

for i in range(len(clusters.centers)):
    #cluster = res.filter(lambda x: x[2]==float(i)).sortBy(lambda x:x[5],ascending=False)  #15mins
    cluster = res.filter(lambda x: x[2]==float(i))
    '''
    if cluster.count()<1000:
        print(cluster.count())
    else:
        re = sc.parallelize(cluster.top(1000,key=lambda x:x[5]))
        print(re.count())
    '''
    totalNum = cluster.count()
    if totalNum > 1000:
        totalNum = 10
        if i == 0:
            pru = sc.parallelize(cluster.top(totalNum,key=lambda x:x[5]))
        else:
            pru = pru.union(sc.parallelize(cluster.top(totalNum,key=lambda x:x[5])))
    else:
        if i == 0:
            pru = cluster
        else:
            pru = pru.union(cluster)
    '''
    if i == 0:
        pru = sc.parallelize(cluster.top(totalNum))
    else:
        pru = pru.union(sc.parallelize(cluster.take(totalNum))) #20mins
    '''
#print(pru.count())

'''
data = data.sortBy(lambda x:x[1],ascending=False)
print(data.collect())
data2 = sc.parallelize(data.take(int(0.5*data.count())))
data = data.union(data2)
print(data.collect())
'''

pru.saveAsTextFile("indexBasedData2.out")
#data = pru
data = data.map(lambda x: [float(x[0]),float(x[1])])
data.cache()
dataCollected = data.collect()
#knnobj = NearestNeighbors().fit(dataCollected)
knnobj = NearestNeighbors(algorithm = 'kd_tree').fit(dataCollected)
bc_knnobj = sc.broadcast(knnobj)
#results = data.map(lambda x: bc_knnobj.value.kneighbors(np.array(x).reshape(1,-1),n_neighbors=1))
pru = pru.map(lambda x:[float(x[0]),float(x[1])])
results = pru.map(lambda x: bc_knnobj.value.kneighbors(np.array(x).reshape(1,-1),n_neighbors=5))
results = results.map(lambda x: (x[1][0][0],x[0][0][4],x[1][0][4]))
#r = results.collect()
#print(len(r))
results.saveAsTextFile("indexBased2.out")











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
