#!/bin/bash

# Clearing File
rm List.txt

dpid=1

file="./ID.txt"
while read line
do 
	# Testing Stability
	echo $line
	echo "Done"	

	Track=$(cat *|grep -n ${line} Master.txt)
	TrackSize=$(grep -n ${line} Master.txt|wc -l)
	# Testing Stability
	echo $Track
	echo $TrackSize
	
	# Writing Descriptive Info
	id=$(grep -e ${line} Master.txt| cut -d '>' -f2| uniq)
	echo -e "${id}\t \c" >> List.txt	
      #	dpid=$(echo ${Track}|cut -d ':' -f1)
      #	dp=$(sed -n $(expr ${dpid} + 3)p Master.txt|cut -d ';' -f1)
      #	dp=$(sed -n $(expr ${dpid} + 4)p Master.txt|cut -d ',' -f4)
      #	echo -e "${dp}\t" >> List.txt	
      # echo "\n\t\t" >> List.txt
	
	# Testing Stability
	echo $dp
	echo $dpid
	
	# Writing Sequence
	COUNT=1
	TrackAddMatrix=$(grep -n ${line} Master.txt|cut -d ":" -f1)
	until [ $COUNT -gt ${TrackSize} ]; do
	#	echo -e "\n" >> List.txt		 
	#	echo -e "\t" >> List.txt		 
	#	echo -e "\t" >> List.txt		 
		TrackAdd=$(echo ${TrackAddMatrix}|cut -d " " -f${COUNT})
	        # dp=$(sed -n $(expr ${TrackAdd} + 4)p Master.txt|cut -d ',' -f4)
	        dp=$(sed -n $(expr ${TrackAdd} + 3)p Master.txt)
        	p1=$(sed -n $(expr ${TrackAdd} + 4)p Master.txt|cut -d ',' -f2)
        	p2=$(sed -n $(expr ${TrackAdd} + 4)p Master.txt|cut -d ',' -f3)
		seq=$(sed -n $(expr ${TrackAdd} + 5)p Master.txt|uniq)
        	if [ $COUNT -eq 1 ]; then
            		echo -e "${dp}\t${p1}\t${p2}\t$seq \c" >> List.txt
        	else
            		TrackAddPre=$(echo ${TrackAddMatrix}|cut -d " " -f$(expr ${COUNT} - 1))
            		seqPre=$(sed -n $(expr ${TrackAddPre} + 5)p Master.txt)
            		if [ "${seq}" != "${seqPre}" ]; then
                		echo -e "${dp}\t${p1}\t${p2}\t$seq \c" >> List.txt
            		fi
        	fi

        	if [ ${COUNT} -lt ${TrackSize} ]; then
			echo -e "\n\t \c" >> List.txt
		fi 
		let COUNT=COUNT+1	
	done
	
      	echo -e "\n \c" >> List.txt
done <"$file"

grep -v '^\s*$' List.txt > FinalList.txt
#sed '/^\s*$/d;/^$/d' List.txt >> FinalList.txt
