import os,sys,csv

#usage: python grepresult.py {dataset} {id_pos}

os.system("head -1 "+sys.argv[1]+" >> resultRows.tsv")
for l in sys.stdin:
    line = l.strip()
    key, value = line.split('\t',1)
    idd = key.split(" ")[int(sys.argv[2])]
    os.system("cat "+sys.argv[1]+" | grep "+idd)
