#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab", sep="\t")

FPKM_values = []


for value in df["FPKM"]:
    if value > 0:
        FPKM_values.append(np.log(value))
        


    
print FPKM_values

plt.hist(FPKM_values)
plt.savefig("day3lunch_problem2.png")
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