#!/bin/bash

mkdir $1
cd $1
cat ../template.py > $1.py
touch rosalind_$1.txt
touch rosalind_sample_$1.txt
touch rosalind_$1_solution.txt
touch rosalind_sample_$1_solution.txt
curl "http://rosalind.info/problems/$1/" > problem.html
python ~/Dev/Bash/getDataset.py > rosalind_sample_$1.txt
python ~/Dev/Bash/getOutput.py > rosalind_sample_$1_solution.txt
gvim -O $1.py rosalind_sample_$1.txt rosalind_sample_$1_solution.txt
