import string, csv, sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
column = 23

reader = None


fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

with open("nbgq-j9jt.tsv","r") as file:
    reader = csv.reader(file,delimiter='\t')
# input comes from STDIN (standard input)
    reader = list(reader)

ds = None
for i in range(1,len(reader),2):
    if len(reader[i]) != column:
        continue
    x_coor = float(reader[i][5])
    y_coor = float(reader[i][13])
    z_coor = float(reader[i][20])
        #print("x: "+x_coor+" y: "+y_coor) 
    ds = ax.scatter(x_coor, y_coor,z_coor, c='g',marker=".",label="Dataset")

with open("resultRows.tsv","r") as file:
    reader = csv.reader(file,delimiter='\t')
# input comes from STDIN (standard input)
    reader = list(reader)

ol = None
for i in range(1,len(reader)):
    if len(reader[i]) != column:
        continue
    x_coor = float(reader[i][5])
    y_coor = float(reader[i][13])
    z_coor = float(reader[i][20])
        #print("x: "+x_coor+" y: "+y_coor) 
    ol = ax.scatter(x_coor, y_coor,z_coor, c='b',marker=".",label="Outliers")
    

plt.legend((ds,ol),("Dataset","Outliers"),loc="lower left")
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_zticklabels([])
ax.set_xlabel('Weighted Registers')
ax.set_ylabel('Year 2015 Formula (in$)')
ax.set_zlabel('Year 2014 Formula (in$)')
ax.set_title('Dataset nbgq-j9jt: Fair Student Funding Budget Detail 2')
plt.savefig("plot.png")
