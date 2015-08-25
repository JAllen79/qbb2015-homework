#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment = '#', header =None)

df.columns = ["Chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

#roi = df["Chromosome"].str.contains("2L")
#print df[roi].shape

#plt.figure()
#plt.plot(df[roi]["start"])
#plt.savefig("starts2L.png")

#roi = df["Chromosome"].str.contains("2R")

#plt.figure()
#plt.plot(df[roi]["start"])
#plt.xlabel("gene")
#plt.savefig("starts2R.png")

#for chromosome in ("2L", "2R", "Y"):
    #roi = df["Chromosome"].str.contains(chromosome)
    #plt.figure()
    #plt.plot(df[roi]["start"])
    #plt.title(chromosome)
    #plt.ylabel("start position")
    #plt.xlabel("gene")
    #plt.savefig("starts" + chromosome + ".png")
    
subset = df["attributes"].str.contains("Sxl")
#plt.figure()
#plt.plot(df[subset]["start"])
#plt.title("Sxl")
#plt.ylabel("start position")
#plt.xlabel("gene")
#plt.savefig("Sxl")

#plt.figure()
#plt.plot(df[subset]["type"].str.contains("transcript"))
#plt.savefig("Day2homework_graph2")

subset2 = df[subset]["type"].str.contains("transcript")

print df[subset][subset2]
plt.figure()
plt.plot(df[subset][subset2]["start"])
plt.title("Sxl, Transcripts only")
plt.ylabel("Start Position")
plt.xlabel("gene")
plt.savefig("Day2homework_graph2")