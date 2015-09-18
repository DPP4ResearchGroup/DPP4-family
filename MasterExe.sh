#!/bin/bash
# This script coordinates all the processes and complete automate the analysisi

# Ask for a result depository folder 
echo "Please create a result depository folder name"
read -e  NewFolder
mkdir $NewFolder


# Run the first master script 
bash 1-MasterRun.sh

# Run the second master script 
bash 2-MasterRun.sh

# Run the Third master script
bash 3-MasterRun.sh


# Clean up the home directory and deposit result to result depository
mv *.txt $NewFolder
mv $NewFolder/TargetDipeptide.txt .
mv -n  NonTarget/ $NewFolder
mv -n Target/  $NewFolder
mv -n Final/ $NewFolder
