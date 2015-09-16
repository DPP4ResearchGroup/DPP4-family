# This program is to generate a target ID list

from Bio import SeqIO

TargetSeq = []
i = 0

"""
AATarget1 = "TargetSequencePosition1.txt"
AATarget2 = "TargetSequencePosition2.txt"

with open (AATarget1, "rU") as fSeq1:
	with open (AATarget2, "rU") as fSeq2:
		AA1 = fSeq1.read()
		AA1 = AA1.strip("\n")
		AA2 = fSeq2.read()
		AA2 = AA2.strip("\n")
		for aa1 in AA1:
			for aa2 in AA2:
				TargetSeq.append (aa1 + aa2)

"""
with open ("TargetDipeptide.txt","rU") as fSeq1:
	for AA in fSeq1:
		AA = AA.strip("\n")
		TargetSeq.append (AA)

#Testing 
print TargetSeq

with open ("FileList.txt","w+") as fFile:
	with open ("RInput.dat","w+") as fW:
		for targetseq in TargetSeq:
			TargetFile = "Seq("+targetseq+")ExtracellularTarget.dat"
			fFile.write (TargetFile+"\n")
			for seq in SeqIO.parse(TargetFile,"fasta"):
				fW.write (seq.id.strip("['" + "'," + "']")+"\n")
 				i=i+1
				print seq.id.strip("['" + "'," + "']")
 
print "Total is "+ str(i)
