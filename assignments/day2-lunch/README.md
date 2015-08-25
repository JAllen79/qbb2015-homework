QBB2015 - Day 2 - Lunch Exercise
================================

Explore the .SAM file generated during last night's homework (/Users/cmdb/qbb2015/day1/SRR072893.sam)

For each question, submit **two** files to your GitHub repository:

- python code
- output

Here's one way to catch the output:

```shell
/Users/cmdb/qbb2015/day2 $ ./day2-exercise2.py > day2-exercise2.out 
```

**Basic Exercises**

1. Count number of alignments
  - HINT: counter variable
2. Count number of alignments that match perfectly to the genome
  - HINT: google sam format optional fields
3. Count number of reads that map to exactly one location in the genome
  - HINT: number of hits
4. For the first 10 alignments, print just the column indicating which chromosome a given read aligns to
  - HINT: .split()
5. Calculate how many alignments are on chromosome 2L 2R 3L 3R 4 X (keep track separately)
  - Use a dictionary!
6. Calculate average MAPQ score
  - HINT 1: counter and total variables
  - HINT 2: if you use split() you will need to convert the string to an integer
7. Count number of reads that start their alignment on chromosome 2L between base 10000 and 20000 (inclusive)
  - HINT: and

**Advanced Exercises**

- Find position at which the most reads start their alignment
  - HINT 1: Python version of `cut -f3,4 accepted_hits.sam | sort | uniq -c | sort -n`
  - HINT 2: google for python "uniq -c"
- How many reads map to the reverse strand?
  - HINT 1: sam flag 0x10 bit
  - HINT 2: stackoverflow.com/questions/2591483/getting-a-specific-bit-value-in-a-byte-string
- Determine how many reads have an average quality score >30
  - HINT 1: fastq wiki phred+33
  - HINT 2: stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
