#!/bin/bash
# This is the first part of the process

echo "Please select your Input UniProt depository file"
read -e File
python Main-V2.py $File

python PtoRList.py
