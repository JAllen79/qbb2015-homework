#!/bin/bash

wget -O BDGP6.Ensembl.81.gtf.gz ftp.ensembl.org/pub/release-81/gtf/drosophila_melanogaster/Drosophila_melanogaster.BDGP6.81.gtf.gz
gunzip BDGP6.Ensembl.81.gtf.gz
wget -O BDGP6.fa.gz ftp.ensembl.org/pub/release-81/fasta/drosophila_melanogaster/dna/Drosophila_melanogaster.BDGP6.dna_sm.toplevel.fa.gz
gunzip BDGP6.fa.gz
