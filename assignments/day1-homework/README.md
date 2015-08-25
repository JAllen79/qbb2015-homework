QBB2015 - Day 1 - Homework
==========================

Perform an RNA-seq analysis on the male stage 10 embryo (SRR072893) using HISAT/StringTie.  Submit:

- commands
- debugged Bash script

**Basic Exercises**

1. Run the following commands to download the StringTie output for [SRP004442](http://www.ncbi.nlm.nih.gov/sra/SRP004442):

    ```shell
    cd /Users/cmdb/qbb2015
    wget http://dl.dropboxusercontent.com/u/169950361/SRP004442.stringtie.tar.gz
    tar xzvf SRP004442.stringtie.tar.gz
    ```

    **NOTE:** This exercise is to prepare for tomorrow's exercises and will not be used for the rest of the homework.

2. Generate a quality control report for the reads in SRR072893.fastq using [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

    - HINT: fastqc -help

    **NOTE:** If you are encountering errors, you may still have a truncated version of SRR072893.fastq.  Try making a fresh copy from /Users/cmdb/rawdata.

3. Map reads to BDGP6 using [HISAT](https://ccb.jhu.edu/software/hisat/index.shtml)

    - HINT: use options -p -S
    
    **NOTE:** Do all the following commands inside /Users/cmdb/qbb2015/day1 to keep your result files organized
    
4. Convert .sam to .bam, sort, and index using [SAMtools](http://www.htslib.org/doc/samtools.html)

    - HINT: samtools view, samtools sort (try Legacy syntax), samtools index

5. Quantitate sorted .bam file using [StringTie](http://ccb.jhu.edu/software/stringtie/)

    - HINT: use options -p -e -G -o -B

6. Debug the qbb2015/assignments/day1-homework/doAnalysis.sh Bash script

    **NOTE:** the output should look something like:
    
    ```
    fastqc /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -o /Users/cmdb/qbb2015/assignments/day1-homework
    hisat -p 4 -x /Users/cmdb/qbb2015/genomes/BDGP6 -U /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -S SRR072893.sam
    fastqc /Users/cmdb/qbb2015/rawdata/SRR072894.fastq.gz -o /Users/cmdb/qbb2015/assignments/day1-homework
    hisat -p 4 -x /Users/cmdb/qbb2015/genomes/BDGP6 -U /Users/cmdb/qbb2015/rawdata/SRR072894.fastq.gz -S SRR072894.sam
                                                 ...
    fastqc /Users/cmdb/qbb2015/rawdata/SRR072916.fastq.gz -o /Users/cmdb/qbb2015/assignments/day1-homework
    hisat -p 4 -x /Users/cmdb/qbb2015/genomes/BDGP6 -U /Users/cmdb/qbb2015/rawdata/SRR072916.fastq.gz -S SRR072916.sam
    ```
    

**Advanced Exercises**

1. Calculate how many alignments are on each chromosome in your .sam file

    - HINT: cut sort uniq

2. Find the chromosome position in your .sam file at which the most reads start their alignment

    - HINT: cut sort uniq sort

3. Calculate the mean FPKM and standard deviation for Sxl transcript FBtr0331261 across all 24 samples in /Users/cmdb/qbb2015/stringtie

    - HINT: grep SRR072*/t_data.ctab | awk

4. Which transcripts have an FPKM > 1000 in all 24 samples?

    - HINT: paste SRR072*/t_data.ctab | cut | awk
