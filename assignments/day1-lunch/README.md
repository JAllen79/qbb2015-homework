QBB2015 - Day 1 - Lunch Exercise
================================

Summarize genome annotation (BDGP6.Ensembl.81.gtf) using Unix tools. Skim over [.GTF format](http://www.ensembl.org/info/website/upload/gff.html) specification. 

**Unix References**

- Codecademy "[Learn the Command Line](https://www.codecademy.com/courses/learn-the-command-line)" course
- Software Carpentry "[The Unix Shell](http://swcarpentry.github.io/shell-novice/)"
- [Cheatsheet](https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-)) of keyboard shortcuts, core commands, etc.
- Wikipedia list of [Unix commands](https://en.wikipedia.org/wiki/List_of_Unix_commands)

**Submitting Answers**

Save output of your final commands in a single file and push into the day1-lunch directory of your qbb2015-homework repo e.g.

```shell
$ cd /Users/cmdb/qbb2015/genomes

$ # NOTE: a single chevron '>' will destroy any existing file named "answers"
$ head BDGP6.fa > answers

$ # NOTE: two chevrons '>>' will add to the end of the file "answers" if it already exists
$ head BDGP6.Ensembl.81.gtf >> answers

$ cd /Users/cmdb/qbb2015-homework
$ mkdir day1-lunch
$ cp ../qbb2015/genomes/answers day1-lunch

$ git status
$ git add day1-lunch/answers
$ git commit -m "All of the answers, correct too!"
$ git push
$ git status
```

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
