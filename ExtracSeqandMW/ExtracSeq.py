import sys
from Bio import SwissProt

# import uniprot file as SwissProt Text format 
Input = sys.argv[-1]
print Input

handle = open (Input, "r")
records = list(SwissProt.parse(handle))
print "Created list for UniProt entries!" 

# create output file 
OutFile = "SeperatedUniProt.txt"
 
import Filter 
Filter.seperation (records,OutFile)



