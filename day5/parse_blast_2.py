#!/usr/bin/env python

"""
Parse a single BLAST record from stdin and print it.
"""

import sys
from blast import BLASTReader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

reader = open ("blast_results.txt")

Score = []
E_Value = []

for line in reader:

    if "Score = " in line:
        fields = line.split()
        Score.append(float(fields[2]))
        E_Value.append(float(fields[7]))
       

print Score
print E_Value
    


plt.figure()
plt.hist(Score)
plt.savefig("day5_histogram_scores.png")

plt.figure()
plt.hist(E_Value)
plt.savefig("day5_histogram_evalues.png")

plt.figure()
plt.scatter(np.log(Score), np.log(E_Value))
plt.xlabel(Score)
plt.ylabel(E_Value)
plt.savefig("day5_scatterplot.png")
#plt.figure()
#plt.bar(range(len(Score)), Score.values())
#plt.xticks(range(len(chromosomes)), chromosomes.values())
#plt.savefig("hist_Score.png")
