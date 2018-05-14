import os,sys,csv

#args 1:raw result 2:result sheet 3:dir name

username = "xz1133"
dirname = sys.argv[3]
rawresult = sys.argv[1]
topn = sys.argv[2]
#obtain files from dumbo
os.system("scp "+username+"@dumbo.hpc.nyu.edu:~/project/src/"+dirname+"/"+rawresult+" .")
os.system("scp "+username+"@dumbo.hpc.nyu.edu:~/project/src/"+dirname+"/"+topn+" .")


#output lines from raw result
c = open(topn)
reader = csv.reader(c,delimiter='\n')
reader = list(reader)
result = reader[1][0].lstrip("[").rstrip("]").split(", ")
for e in result:
    os.system("cat "+rawresult+" | grep "+e)

