#!/bin/bash

## Pick Up Search Pattern
#iHSA=$(grep -o hsa Code.txt|wc -w)		# Number of Pathway in File Code.txt
#HSA=$(cat * Code.txt)

## Testing Stabiltiy 
#echo $iHSA
#echo $HSA

MAINCOUNT=1

file="./FSortCode.txt"
while read line 
do
	# Testing Stability
	#echo "$line"
	#echo "Done"
	
	# Searching Substrates under each Pathway
	LINE=$(echo ${line}|awk '{print $2}')
	#echo "LINE ${LINE}"	

	SP=$(cat *|grep -n ${LINE} Pathway.txt)
	SPLen=$(cat *|grep -c ${LINE} Pathway.txt)
	
	# Testing Stability 
	#echo $SP 		
	#echo $SPLen
	
	# Counter Zero
	COUNT=1
	HSACounter1=0
	HSACounter2=0
	TrackCounter=0
		
	# Writing Final File
	HSACounter1=$(($MAINCOUNT+4*($MAINCOUNT - 1)))
	HSACounter2=$(($MAINCOUNT+4*($MAINCOUNT - 1)+1))		
	# Testing Stability
	echo "HSACounter1 ${HSACounter1}"
	echo "HSACounter2 ${HSACounter2}"
	
	sed -n ${HSACounter1}p AFSortCode.txt >> Final.txt
	sed -n ${HSACounter2}p AFSortCode.txt >> Final.txt
	echo -e "\n" >> Final.txt

	# Searching for Substrate UniProt Number 
	until [ $COUNT -gt $SPLen ]; do
		# Testing Stability
	 	#echo "COUNT ${COUNT}"
		# Testing Output Entry		
		#echo $SP| cut -d ' ' -f$COUNT
		
		HSAEntry=$(echo $SP| cut -d ' ' -f$COUNT)
		UniProtEntry=$(expr $(echo $HSAEntry| cut -d ':' -f1) - 1)
		# Testing Stability
		#echo $UniProtEntry
		
	#	# Writing Final File
	#	HSACounter1=$(($COUNT+4*($COUNT - 1)))
	#	HSACounter2=$(($COUNT+4*($COUNT - 1)+1))		
	#	# Testing Stability
	#	echo "HSACounter1 ${HSACounter1}"
	#	echo "HSACounter2 ${HSACounter2}"
	#
	#	sed -n ${HSACounter1}p AFSortCode.txt >> Final.txt
	#	sed -n ${HSACounter2}p AFSortCode.txt >> Final.txt
	#	echo -e "\n" >> Final.txt
	
		# Writing UniProt Number to File
		sed -n ${UniProtEntry}p Pathway.txt >> Final.txt
	
		# Writing UniProt Information		
		UniProtID=$(sed -n ${UniProtEntry}p Pathway.txt| cut -d ':' -f2)	
		Track=$(grep -n $UniProtID ./Target/*.dat)						# Searching UniProt ID from Substrate List 
		TrackSize=$(grep -n $UniProtID ./Target/*.dat|wc -l) 
	#	TrackCounter=$(echo $Track| cut -d ":" -f2)
		# Testing 
		echo $Track
		echo "TrackSize ${TrackSize}"
	#	echo "TrackCounter ${TrackCounter}"

		# Writing UniProt Record
		UPCOUNT=1
		until [ $UPCOUNT -gt $TrackSize ]; do 
			TrackAdd=$(echo $Track| cut -d '.' -f$((2 * ${UPCOUNT})))
			TrackAdd=".${TrackAdd}.dat"
			TrackCounter=$(echo $Track| cut -d ":" -f$((2 *${UPCOUNT})))
			echo "TrackAddress ${TrackAdd}"
			echo "TrackCounter ${TrackCounter}"

			sed -n ${TrackCounter},$(($TrackCounter + 6))p $TrackAdd >> Final.txt
			let UPCOUNT=UPCOUNT+1
		done

		# Formating 
		echo -e "\n" >> Final.txt
		let COUNT=COUNT+1
	done
	echo -e "\n\n" >> Final.txt
	let MAINCOUNT=MAINCOUNT+1
done<"$file" 
