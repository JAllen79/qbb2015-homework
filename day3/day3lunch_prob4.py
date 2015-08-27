#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab", sep="\t")["FPKM"]
df2 = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072899/t_data.ctab", sep="\t")["FPKM"]

#FPKM_values_df =  []
#FPKM_values_df2 = []

#for value in df["FPKM"]:
    #if value > 0:
        #FPKM_values_df.append(value)
#        FPKM_values.append(np.log(value))
binmaskdf = df != 0
binmaskdf2 = df2 != 0
#for value in df2["FPKM"]:
    #if value > 0:
        #FPKM_values_df2.append(value)
binmaster = binmaskdf & binmaskdf2
intermdf = df[binmaster].values
intermdf2 = df2[binmaster].values        
M = np.log2(intermdf) - np.log2(intermdf2)
A = (0.5)*((np.log2(intermdf)) + (np.log2(intermdf2)))

plt.figure()
plt.scatter(M, A)
plt.xlabel("M")
plt.ylabel("A")
plt.savefig("MAPlot.png")


        
#FPKM_values_ = pd.Series(np.random.randn(1000))        
#FPKM_values.plot(kind='kde')
#plt.savefig("day3lunch_problem3.png")



    
#print FPKM_values
#plt.hist(FPKM_values)
#plt.savefig("day3lunch_problem2.png")
#plt.figure()
#plt.bar(range(len(chromosomes)), chromosomes.values())
#plt.xticks(range(len(chromosomes)), chromosomes.values())
#plt.savefig("Barplot.png")

#Sxl = []

#for sample in metadata[metadata["sex"] == "female"]["sample"]:
#    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
 #   roi = df["t_name"].str.contains("FBtr0331261")
  #  df[roi]["FPKM"].values
   # Sxl.append(df[roi]["FPKM"].values)