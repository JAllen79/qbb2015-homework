QBB2015 - Day 1 - Lunch Exercise
================================

Summarize genome annotation (BDGP6.Ensembl.81.gtf) using Unix tools.  Skim over [.GTF format](http://www.ensembl.org/info/website/upload/gff.html) specification. Submit:

- stdout of each command

**Basic Exercises**

1. How many lines are there?

    - HINT: wc

2. How many lines deal with the gene Sxl?

    - HINT: grep option

3. What types of features are there?

    - HINT: cut column 3 sort uniq

4. How many of each feature type are there?

    - HINT: uniq option


**Advanced Exercises**

1. For the first 100 features, report the chromosome, strand, start, end, and length

    - HINT: grymoire.com/Unix/Awk.html

2. Calculate the average length of all the features

    - HINT: END NR

3. Filter for features on the plus strand with a length greater than the average length

    - HINT: &&

4. For each feature, print ecah attribute on a separate line with tag and value separated by a tab

    - HINT: split for loop
