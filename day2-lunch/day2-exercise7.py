#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open(filename)
#line_count = 0
#for line in f:
#    line_count += 1
    
    
#print "This is Question 1"
#print line_count - 1

reads_2L = 0
#total = 0

for line in (f):
    if line[0] != "@":
        #if line_count < 10:
        split_columns = line.split()
        if str(split_columns[2]) == "2L" and float(split_columns[3]) >= 10000 and float(split_columns[3]) <= 20000:
            reads_2L += 1
            
print reads_2L
        #if str(split_columns[2]) in align_count:
            #align_count[str(split_columns[2])] += 1
            
#print align_count
            #print split_columns[2]
            #line_count += 1
        #else:
            #break

#perfect_matches = 0
#for line in (f):
    #if "NH:i:1" in line:
        #perfect_matches += 1
    #else: 
        #pass
            
#print perfect_matches