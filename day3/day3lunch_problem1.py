#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axis as axis

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
new_reps = pd.read_csv("~/qbb2015/rawdata/replicates.csv")

Sxl = []

for sample in metadata[metadata["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    df[roi]["FPKM"].values
    Sxl.append(df[roi]["FPKM"].values)
    
Sxl_male = []

for sample in metadata[metadata["sex"] == "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    df[roi]["FPKM"].values
    Sxl_male.append(df[roi]["FPKM"].values)
    
Sxl_repl_female = []

for sample in new_reps[new_reps["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    df[roi]["FPKM"].values
    Sxl_repl_female.append(df[roi]["FPKM"].values)
    
Sxl_repl_male = []

for sample in new_reps[new_reps["sex"] == "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    df[roi]["FPKM"].values
    Sxl_repl_male.append(df[roi]["FPKM"].values)
    
x_ticks = []    
    
for x in metadata["stage"][0:8]:
    x_ticks.append(x)
    
print x_ticks
        
#plt.figure()
#plt.plot(Sxl)
#plt.plot(Sxl_male)
#plt.savefig("Timecourse.png")

    
#Sxl_male = []

#for sample in metadata[metadata["sex"] == "male"]["sample"]:
    #df2 = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    #roi2 = df["t_name"].str.contains("FBtr0331261")
    #df2[roi2]["FPKM"].values
    #Sxl_male.append(df[roi]["FPKM"].values)


    
plt.figure()
plt.title("Sxl")
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.plot(Sxl, "b-", label="female")
plt.plot(Sxl_male, "r-", label="male")
plt.plot([4,5,6,7], Sxl_repl_female, "bo")
plt.plot([4,5,6,7], Sxl_repl_male, "ro")
plt.xticks(range(8), x_ticks)
plt.legend(bbox_to_anchor=(0.5, 1))
plt.savefig("day3lunch_problem1.png")
