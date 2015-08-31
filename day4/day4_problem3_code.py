#!/usr/bin/env python

"""
testing of chrombits_good.py code
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib_venn as venn
import sys
import chrombits_good

arr = chrombits_good.ChromosomeLocationBitArrays(fname=sys.argv[1])

CTCF = arr.copy()
BEAF = arr.copy()
SuHW = arr.copy()

CTCF.set_bits_from_file(sys.argv[2])
BEAF.set_bits_from_file(sys.argv[3])
SuHW.set_bits_from_file(sys.argv[4])

#program = BEAF.intersect(CTCF.complement())
#program2 = program.a_and_not_b()

prog3 = CTCF.union(BEAF).union(SuHW)

Tuples = prog3.a_and_not_b()

Abc = 0
aBc = 0
abC = 0
ABc = 0
aBC = 0
AbC = 0
ABC = 0

for x in Tuples:
    chrom, start, end = x
    if np.any(CTCF.arrays[ chrom ][start : end]):
        if np.any(BEAF.arrays[chrom][start : end]):
            if np.any(SuHW.arrays[chrom][start : end]):
                ABC += 1
            else:
                ABc += 1
        else: 
            if np.any(BEAF.arrays[chrom][start : end]):
                AbC += 1
            else:
                Abc += 1
    else:
        if np.any(BEAF.arrays[chrom][start : end]):
            if np.any(SuHW.arrays[chrom][start : end]):
                aBC += 1
            else:
                aBc += 1
        else:
            if np.any(SuHW.arrays[chrom][start : end]):
                abC += 1
            else:
                abc +=1
                
plt.figure()
venn.venn3((Abc, aBc, ABc, abC, AbC, aBC, ABC), set_labels=(CTCF, BEAF, SuHW))
plt.savefig("day4_problem3_venn")