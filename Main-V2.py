import sys
Input = sys.argv[-1]
print Input

#Globle File Management
#Input="uni.mouse.txt"					# Globle File Input
#Input="UniProt.dat"
#Input="MF2.dat"
#Input="HumanReview.txt"					# Globle File Input
#Testing 
#Input = "GLP.txt"
"""
AATarget1 = "TargetSequencePosition1.txt"
AATarget2 = "TargetSequencePosition2.txt"
"""

# Zero Variables
TargetSeq = []
GlobalStat = 0

from Bio import SwissProt
handle = open (Input,"r")
records = list(SwissProt.parse(handle))
print "Done Big List Parsing"

"""
HumanOut="HumanAccessions.txt"				# Human Protein Accession File 
							# (This need to be fasta format for later Analysis) 
HumanMAPInput=HumanOut
HumanMAPOut="HumanMAPList.txt"
	
AlignInput="HumanMAPList.txt"				# This is a File Name (used in SeqIO.parse)
MAPUpdateOutPut="HumanMAPFiltered.txt"

CytoMitoInput=MAPUpdateOutPut
CytoOutput="CytoList.txt"
MitoOutput="MitoList.txt"
"""

"""
InputSeqRecord=MAPUpdateOutput
InputSeqFullRecord=Input
"""

"""
#Global Parameter Setup
SimilarityCutOffRate=0.98
"""
"""
#Sort Human Proteins from UniProt Proteins
import ModuleHuman
ModuleHuman.HumanProtein(records,HumanOut)
"""


#Apply Filter to filter DPP proteins
"""
with open (AATarget1,"rU") as fSeq1:
	with open (AATarget2,"rU") as fSeq2:
		AA1 = fSeq1.read()
		AA1 = AA1.strip("\n")
		AA2 = fSeq2.read()
		AA2 = AA2.strip("\n")
		for aa1 in AA1:
			for aa2 in AA2:
				TargetSeq.append(aa1+aa2) 
"""

with open ("TargetDipeptide.txt","rU") as fSeq1:
	for AA in fSeq1:
		AA = AA.strip("\n") 
		TargetSeq.append(AA)
print TargetSeq

# Generating File Cluster for each DPP Consensus search:
FullRecord=records


"""
import ModuleHumanMAP
ModuleHumanMAP.MAPFilter(HumanMAPInput,HumanMAPOut)
"""
"""
#In order to Filter duplication, Alignment is needed
import ModuleAln
ModuleAln.Aln(AlignInput,MAPUpdateOutPut,SimilarityCutOffRate)		# Aln(AlignInput,FilteredList,SimilarityCutOffRate)

#This step Separate Lists into Mito and Cyto
import ModuleMitoCytoFilter
ModuleMitoCytoFilter.CytoMitoFilter(CytoMitoInput,CytoOutput,MitoOutput)
"""


###This step is used to separate Peptides into designed Catagories
import ModulePepProcess

## Global Stat File
with open ("GlobalStat.txt","w") as Stat:
	## File Name generation
	for targetseq in TargetSeq: 
		OutputFileM="Seq("+targetseq+")MitoTarget.dat"
		OutputFileMN="Seq("+targetseq+")MitoNonTarget.dat"
		OutputFileCyto="Seq("+targetseq+")CytoTarget.dat"
		OutputFileCytoN="Seq("+targetseq+")CytoNonTarget.dat"
		OutputFileExtra="Seq("+targetseq+")ExtracellularTarget.dat"
		OutputFileExtraN="Seq("+targetseq+")ExtracellularNonTarget.dat"

		#SeparationFilter(FullRecord,TargetSeq,OutputFileM,OutputFileExtra,OutputFileCyto,OutputFileMN,OutputFileExtraN,OutputFileCytoN)
		ModulePepProcess.SeparationFilter(FullRecord,targetseq,OutputFileM,OutputFileExtra,OutputFileCyto,OutputFileMN,OutputFileExtraN,OutputFileCytoN)
		
		#Write Global Stiat File
		GlobalStat = ModulePepProcess.GlobalStatTarget
		GlobalStatNon = ModulePepProcess.GlobalStatNonTarget
		print "Validation GlobalStat"
		print GlobalStat
		print GlobalStatNon
		Stat.write (OutputFileExtra + "\n")
		Stat.write ("Total "+str(GlobalStat)+"Found"+"\n")
		Stat.write ("\n")		
		Stat.write (OutputFileExtraN + "\n")
		Stat.write ("Total "+str(GlobalStatNon)+"Found"+"\n")
		Stat.write ("\n")		
		Stat.write (OutputFileExtra + OutputFileExtraN + "\n")
		Stat.write ("Total "+str(GlobalStat+GlobalStatNon)+"Found"+"\n")
		Stat.write ("\n")		

"""
##Separate Mito List
InputSeqRecord=MitoOutput	# Testing 	"HumanAccessions.txt" 
FullRecord=records
OutputFileM="MitoM.txt"
OutputFilePep="MitoPep.txt"
OutputFileChain="MitoChain.txt"

#SeparationFilter(InputSeqRecord,FullRecord,OutputFileM,OutputFilePep,OutputFileChain)
ModulePepProcess.SeparationFilter(InputSeqRecord,FullRecord,OutputFileM,OutputFilePep,OutputFileChain)
"""
