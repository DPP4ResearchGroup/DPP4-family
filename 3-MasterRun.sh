#!/bin/bash

# Generating Master.txt file
bash masterlist.sh

# Generating Unique TargetID
cat RInput.dat | uniq > ID.txt

# Generate the final table 
bash SubstrateList.sh

# Relocate the final xlsx file into ./Final Directory 
mv FinalList.txt ./Final
