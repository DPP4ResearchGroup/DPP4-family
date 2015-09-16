# Copy all the filtered .dat files to Target folder
# Note: Change working directory
# Note: Change file name to be more informative


#!/bin/bash

# Prepare Directories 
mkdir Target
mkdir NonTarget
mv *ExtracellularTarget.dat Target 
mv Seq*.dat NonTarget

# RTest.R to get Pathway.txt file
Rscript RTest.R

# Filtering Pathway.txt file to get Code.txt
grep hsa* Pathway.txt > Code.txt

# Sorting Code.txt to get FSortCode.txt
sort Code.txt| uniq -c | sort > FSortCode.txt

# Run PathwaySorting.R to get AFSortCode.txt
Rscript PathwaySorting.R

# Run run.sh to get Final.txt file
bash run.sh

# Rename Refolder
mkdir Final
mv Final* Final
