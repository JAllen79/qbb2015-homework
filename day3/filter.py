#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"
import sys
#print sys.argv
#filename = sys.argv[1]

#f = open(filename)

#for line in f:
    #fields = line.split()
    #if "tRNA" in fields[9]:
        #print line,

f = sys.stdin

name_counts = {}
        
for line_count, line in enumerate(f):
    fields = line.split()
    gene_name = fields[9]
    if gene_name not in name_counts:
        name_counts[gene_name] = 1
    else:
        name_counts[gene_name] += 1

#Iterate key, value pairs from the name counts dictionary
for key, value in name_counts.iteritems():
    #print gene name and counts
    print key, value    
    
    