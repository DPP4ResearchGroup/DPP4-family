inputfilename = "MouseFinalList.txt"
#inputfilename = "HumanFinalList-3.txt"
outputfilename = "Human.fasta"
outputfilename = "Mouse.fasta"

import csv 

ids = []
discripts = []
seqs = []

rfile = open (inputfilename,"rU")
csv_file = csv.reader(rfile,delimiter = "\t")

with open (outputfilename,"w") as wfile: 
	for id,discript,seq in csv_file: 
		fasta = ">"+ id + "|" + discript + "\n" + seq + "\n"
		wfile.write (fasta)
rfile.close()
wfile.close()

