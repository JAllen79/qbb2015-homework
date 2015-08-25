#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment = '#', header =None)

#print df
#print df.head()
#print df.describe()
#print df.info()
#print df[1:5] #prints rows 1-4
#print df[9:15] #shows rows 10-15 (1-based, inclusive)
#print df[19:25]

#print df.info() #prints column names
df.columns = ["Chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"] #names columns of df
#print df.info()

#print df.sort("type", ascending=False) #sort() takes arguments, must be in right order unless key words used, e.g. column = "type", ascending=False

#print df["Chromosome"]
#print df[["Chromosome", "start", "end"]]

#print df["start"][9:15]
#print df.shape
df2 = df["start"]
#print df2.shape

#df2.to_csv("startColumn.txt")  #saves df2 using panda to_csv format, makes txt
#df2.to_csv("startColumn.txt", sep='\t', index = False)
#print df.shape
ROI = df["start"] < 10
#print ROI
#print type(ROI)
#print ROI.shape
#print df[ROI]
print df[ROI].shape