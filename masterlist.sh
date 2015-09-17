#!/bin/bash

rm Master.txt
# Picking up File Pattern 
file="FileList.txt"
while read line
do 
 sed '1,3d;$d;/^$/d' ./Target/${line} >> Master.txt
done<"$file"
