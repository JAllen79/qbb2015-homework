#!/usr/bin/env python

"""
Count intersection of two BED files
"""

from __future__ import division     #imports good division function that returns floats instead of integers
from matplotlib import pyplot as plt
from matplotlib_venn import venn3
import sys
import numpy

def arrays_from_len_file(fname):
    arrays = {}                 #empty dictionary of each chromosome and its size
    for line in open(fname):
        fields = line.split()   #splits data into fields by white space
        name = fields[0]        #chromosome name is first field, the key
        size = int(fields[1])   #chromosome size is second field
        arrays[name] = numpy.zeros(size, dtype=bool)    #creates an array for each chromosome with an array of zeros, where number of zeros is size
    return arrays       #populates the arrays dictionary, its a dictionary where key is name and values are array
    

def set_bits_from_files(arrays, fname):     #Takes empty (0) array from previous function for specified file name
    for line in open (fname):
        fields = line.split()
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        arrays[chrom][start:end] = 1        

arrays = arrays_from_len_file(sys.argv[1])      #sys.argv[1] takes first input (total chromosome) on command line for the function
set_bits_from_files(arrays, sys.argv[2])        #sys.argv[2] takes second input (conserved regions) to mark all conserved regions of chrom with "1"
arrays_BEAF = arrays_from_len_file(sys.argv[1])
set_bits_from_files(arrays_BEAF, sys.argv[3])
arrays_SuHw = arrays_from_len_file(sys.argv[1])
set_bits_from_files(arrays_SuHw, sys.argv[4])

#for key, value in arrays.iteritems():
#    print key, type(value), value.shape, numpy.sum(value)

total_CTCF_CTCF = 0
any_overlap_CTCF_CTCF = 0
all_overlap_CTCF_CTCF = 0
half_overlap_CTCF_CTCF = 0

for line in open (sys.argv[2]):         #sys.argv[3] is the chrom area where the specified protein acts as transcription factor
    fields = line.split()
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    sl = arrays[chrom][start:end]
    total_CTCF_CTCF += 1                          #specifies total size of area transcription factor is acting
    any_overlap_CTCF_CTCF += sl.any()             #specifies number of places where any base overlaps
    all_overlap_CTCF_CTCF += sl.all()             #specifies only places where arg3 completely overlaps
    if len(sl) > 0:
        half_overlap_CTCF_CTCF += (numpy.sum(sl)/len(sl) > 0.5)   #specifies places where at least half overlap

total_CTCF_BEAF = 0
any_overlap_CTCF_BEAF = 0
all_overlap_CTCF_BEAF = 0
half_overlap_CTCF_BEAF = 0

for line in open (sys.argv[3]):         #sys.argv[3] is the chrom area where the specified protein acts as transcription factor
    fields = line.split()
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    sl = arrays[chrom][start:end]
    total_CTCF_BEAF += 1                          #specifies total size of area transcription factor is acting
    any_overlap_CTCF_BEAF += sl.any()             #specifies number of places where any base overlaps
    all_overlap_CTCF_BEAF += sl.all()             #specifies only places where arg3 completely overlaps
    if len(sl) > 0:
        half_overlap_CTCF_BEAF += (numpy.sum(sl)/len(sl) > 0.5)   #specifies places where at least half overlap
    
total_CTCF_SuHW = 0
any_overlap_CTCF_SuHw = 0
all_overlap_CTCF_SuHw = 0
half_overlap_CTCF_SuHw = 0
    
for line in open (sys.argv[4]):        
    fields = line.split()
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    sl = arrays[chrom][start:end]
    total_CTCF_SuHW += 1
    any_overlap_CTCF_SuHw += sl.any()
    all_overlap_CTCF_SuHw += sl.all()
    half_overlap_CTCF_SuHw += (numpy.sum(sl)/len(sl) > 0.5) 
    
#print "Total_CTCF_BEAF: %d, Any overlap_CTCF_BEAF: %d, All overlap_CTCF_BEAF: %d, Half overlap_CTCF_BEAF: %d" % (total_CTCF_BEAF, any_overlap_CTCF_BEAF, all_overlap_CTCF_BEAF, half_overlap_CTCF_BEAF)
#print "Total_CTCF_Su(Hw): %d, Any overlap_CTCF_Su(Hw): %d, All overlap_CTCF_Su(Hw): %d, Half overlap_CTCF_Su(Hw): %d" % (total_CTCF_Su(Hw), any_overlap_CTCF_Su(Hw), all_overlap_CTCF_Su(Hw), half_overlap_CTCF_Su(Hw))

total_BEAF_BEAF = 0
any_overlap_BEAF_BEAF = 0
all_overlap_BEAF_BEAF = 0
half_overlap_BEAF_BEAF = 0

for line in open (sys.argv[3]):         #sys.argv[3] is the chrom area where the specified protein acts as transcription factor
    fields = line.split()
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    sl = arrays_BEAF[chrom][start:end]
    total_BEAF_BEAF += 1                          #specifies total size of area transcription factor is acting
    any_overlap_BEAF_BEAF += sl.any()             #specifies number of places where any base overlaps
    all_overlap_BEAF_BEAF += sl.all()             #specifies only places where arg3 completely overlaps
    if len(sl) > 0:
        half_overlap_BEAF_BEAF += (numpy.sum(sl)/len(sl) > 0.5)  #specifies places where at least half overlap

total_BEAF_SuHw = 0
any_overlap_BEAF_SuHw = 0
all_overlap_BEAF_SuHw = 0
half_overlap_BEAF_SuHw = 0

for line in open (sys.argv[4]):         #sys.argv[3] is the chrom area where the specified protein acts as transcription factor
    fields = line.split()
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    sl = arrays_BEAF[chrom][start:end]
    total_BEAF_SuHw += 1                          #specifies total size of area transcription factor is acting
    any_overlap_BEAF_SuHw += sl.any()             #specifies number of places where any base overlaps
    all_overlap_BEAF_SuHw += sl.all()             #specifies only places where arg3 completely overlaps
    half_overlap_BEAF_SuHw += (numpy.sum(sl)/len(sl) > 0.5)   #specifies places where at least half overlap    
    
total_SuHw_SuHw = 0
any_overlap_SuHw_SuHw = 0
all_overlap_SuHw_SuHw = 0
half_overlap_SuHw_SuHw = 0

for line in open (sys.argv[4]):         #sys.argv[3] is the chrom area where the specified protein acts as transcription factor
    fields = line.split()
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    sl = arrays_SuHw[chrom][start:end]
    total_SuHw_SuHw += 1                          #specifies total size of area transcription factor is acting
    any_overlap_SuHw_SuHw += sl.any()             #specifies number of places where any base overlaps
    all_overlap_SuHw_SuHw += sl.all()             #specifies only places where arg3 completely overlaps
    half_overlap_SuHw_SuHw += (numpy.sum(sl)/len(sl) > 0.5)   #specifies places where at least half overlap
    
total_SuHw_BEAF_CTCF = 0
any_overlap_SuHw_BEAF_CTCF = 0
all_overlap_SuHw_BEAF_CTCF = 0
half_overlap_SuHw_BEAF_CTCF = 0

for line in open (sys.argv[4]):         #sys.argv[3] is the chrom area where the specified protein acts as transcription factor
    fields = line.split()
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    sl = (arrays_BEAF[chrom][start:end]) & (arrays[chrom][start:end])
    total_SuHw_BEAF_CTCF += 1                          #specifies total size of area transcription factor is acting
    any_overlap_SuHw_BEAF_CTCF += sl.any()             #specifies number of places where any base overlaps
    all_overlap_SuHw_BEAF_CTCF += sl.all()             #specifies only places where arg3 completely overlaps
    half_overlap_SuHw_BEAF_CTCF += (numpy.sum(sl)/len(sl) > 0.5)   #specifies places where at least half overlap
    
#print "Total Overlaps: CTCF-CTCF: %d, CTCF-BEAF: %d, CTCF-SuHW: %d, BEAF-BEAF: %d, BEAF-SuHw: %d, SuHw-SuHw: %d, SuHw-BEAF-CTCF: %d" % (total_CTCF_CTCF, total_CTCF_BEAF, total_CTCF_SuHW, total_BEAF_BEAF, total_BEAF_SuHw, total_SuHw_SuHw, total_SuHw_BEAF_CTCF)
#venn3(subsets = (total_CTCF_CTCF, total_CTCF_BEAF, total_CTCF_SuHW, total_BEAF_BEAF, total_BEAF_SuHw, total_SuHw_SuHw, total_SuHw_BEAF_CTCF), set_labels = ('CTCF', 'BEAF', 'SuHw'))
#plt.show()

print "Half Overlaps: CTCF-CTCF: %d, CTCF-BEAF: %d, CTCF-SuHW: %d, BEAF-BEAF: %d, BEAF-SuHw: %d, SuHw-SuHw: %d, SuHw-BEAF-CTCF: %d" % (total_CTCF_CTCF, total_CTCF_BEAF, total_CTCF_SuHW, total_BEAF_BEAF, total_BEAF_SuHw, total_SuHw_SuHw, total_SuHw_BEAF_CTCF)
venn3(subsets = (half_overlap_CTCF_CTCF, half_overlap_CTCF_BEAF, half_overlap_CTCF_SuHw, half_overlap_BEAF_BEAF, half_overlap_BEAF_SuHw, half_overlap_SuHw_SuHw, half_overlap_SuHw_BEAF_CTCF), set_labels = ('CTCF', 'BEAF', 'SuHw'))
plt.title("Half-Overlaps")
plt.savefig("day4lunch_Venn")