#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df = pd.read_table(annotation)
ROI = df["FPKM"] > 0
print df[ROI]
df1 = df["FPKM"]
top = df1[0:11572]
middle = df1[11572:22144]
end = df1[22144:34718]

plt.figure()
plt.title("Exercise4")
plt.boxplot([top, middle, end])
plt.xlabel("gene")
plt.ylabel("Start Position")
plt.savefig("Exercise4.png")


