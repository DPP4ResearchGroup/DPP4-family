# This module is used to seperate Mit or Cyto into designed categories

"""
# Testing 
InputSeqRecord="HumanAccessions.txt"
InputSeqFullRecord="Trial.dat"
OutputFileM="TesteeM.txt"
OutputFilePep="TesteePep.txt"
OutputFileChain="TesteeChain.txt"
"""

"""
# Functions used in this module
# ListProduce produce a trace for valid accession entries
def ListProduce(InputSeqRecord,FunctionalList):	 
	from Bio import SeqIO
	records=list(SeqIO.parse(InputSeqRecord,"fasta"))
	with open(FunctionalList,"w") as f:
		for record in records:
			f.write(">{0}\n".format(record.id))
			f.write("\n")

def WriteFM (fOF,accession,listee,record,PositionA,PositionB):
	fOF.write (">{0}\n".format(accession.id))
	fOF.write ("\t{0}\n".format(listee))
	fOF.write ("\tRemoved Peptide\n")	
	fOF.write ("\t{0}\n".format(str(record.sequence[(PositionA-1):PositionB])))	
	fOF.write ("\tProcessed Peptide\n")	
	fOF.write ("\t{0}\n".format(record.sequence[PositionB:]))			
	fOF.write ("\n")
	
def WriteF (fOF,accession,listee,record,PositionA,PositionB):
	fOF.write ("\t{0}\n".format(listee))
	fOF.write ("\t{0}\n".format(str(record.sequence[(PositionA-1):PositionB])))		
	fOF.write ("\n")

def ProcessedPepWrite(FeatureList,fOF,accession,record):
    for listee in FeatureList:
	if ("PEPTIDE" in listee) or ("PROPEP" in listee) or ("SIGNAL" in listee):
		PositionA = listee[1] 
		PositionB = listee[2]
		WriteF (fOF,accession,listee,record,PositionA,PositionB)
		for listeeDummy in FeatureList:
			if ("CHAIN" in listee):
				PositionA = listeeDummy[1] 
				PositionB = listeeDummy[2]
				if (isinstance(PositionA,int) and not (isinstance(PositionB,int))):
					PositionB = record.sequence_length
				elif (not (isinstance(PositionA,int)) and not (isinstance(PositionB,int))):
					PositionA = 1 
					PositionB = record.sequence_length				
				WriteF (fOF,accession,listee,record,PositionA,PositionB)
"""

# SeparationFilter is the Major Function in this Module 
def SeparationFilter(FullRecords,TargetSeq,OutputFileM,OutputFileExtra,OutputFileCyto,OutputFileMN,OutputFileExtraN,OutputFileCytoN):  

### def SeparationFilter(FullRecords,TargetSeq,OutputFileM,OutputFileExtra,OutputFileCyto):		#(InputSeqRecord,FullRecords,OutputFileM,OutputFilePep,OutputFileChain):

	"""
	# Specify Functional Accession Numbers for Data Extraction
	FunctionalList="FunctionalAccessions.txt"								# This is an internal list used for AccessNumber Tracking 

	ListProduce(InputSeqRecord,FunctionalList)								# Using Function ListProduce to produce a tracking List for valid Accession Numbers
	"""
	from Bio import SeqIO
									#AccessionList=list(SeqIO.parse(FunctionalList,"fasta"))
	# Counter Zero
	i=0
	j=0
	k=0

	with open (OutputFileM,"w") as fOFM:
	 fOFM.write ("#This file contains mito proteins\n")
	 fOFM.write ("\n")
	 fOFM.write ("\n")

	 with open (OutputFileExtra,"w") as fOFE:
	  fOFE.write ("#This file contains Extracellular Proteins\n")
	  fOFE.write ("\n")
	  fOFE.write ("\n")

	  with open (OutputFileCyto,"w") as fOFC:
	   fOFC.write ("#This file contains Cyto Proteins\n")
	   fOFC.write ("\n")
	   fOFC.write ("\n")

	   with open (OutputFileExtraN,"w") as fOFEN:
	   	fOFEN.write ("#This file contains Extracellular Proteins NonTarget\n")
	 	fOFEN.write ("\n")
	 	fOFEN.write ("\n")
	  	
		for record in FullRecords:
		    KeyWordList=list(record.keywords)
		    FeatureList=list(record.features)
		    # Testing
		    # print FeatureList
		    print TargetSeq
		    for keyword in KeyWordList:
			if ("Secreted" in str(keyword)) or ("secreted" in str(keyword)):
			   for listee in FeatureList:
				# Testing
				print listee
				for Element in listee:
				    # Testing
				    if ("PEPTIDE" in str(Element)) or ("CHAIN" in str(Element)) or ("SIGNAL" in str(Element)):
					# Testing
					print str(listee[1]).find("?")
					if (str(listee[1]).find("?")!=-1) or (str(listee[1]).find("<")!=-1) or (str(listee[1]).find(">")!=-1):
						PositionA = 1
						PositionB = listee[2]
						# Testing 
						print PositionA, PositionB
					elif (str(listee[2]).find("?")!=-1) or (str(listee[2]).find("<")!=-1) or (str(listee[2]).find(">")!=-1):
						PositionA = listee[1]
						PositionB = record.sequence_length
						print PositionA, PositionB
					else: 
						PositionA = listee[1]
						PositionB = listee[2]
					# Testing 
					print "Found One"
					print PositionA
					print PositionB
					
					# Testing
					# print TargetSeq

					# Testing
					print record.sequence[(PositionA-1):(PositionA+1)] 
					print TargetSeq	


					if (record.sequence[(PositionA-1):(PositionA+1)] == TargetSeq):		
						# Testing
						# print record.sequence[(PositionA-1):PositionB] 
						# print TargetSeq		
						
						if (abs(PositionA-PositionB) <= 120):		
							fOFE.write (">{0}\n".format(record.accessions))
							fOFE.write ("\t{0}\n".format(record.entry_name))
							fOFE.write ("\t{0}\n".format(record.keywords))
							fOFE.write ("\t{0}\n".format(record.description))
							fOFE.write ("\t{0}\n".format(listee))
							fOFE.write ("\t{0}\n".format(str(record.sequence[(PositionA-1):PositionB])))	
							fOFE.write ("\n")
							i+=1 		# Counter i for target protein counting 
							# Testing
							print "Save One"
						else:
							fOFEN.write (">{0}\n".format(record.accessions))
							fOFEN.write ("\t{0}\n".format(record.entry_name))
							fOFEN.write ("\t{0}\n".format(record.keywords))
							fOFEN.write ("\t{0}\n".format(record.description))
							fOFEN.write ("\t{0}\n".format(listee))
							fOFEN.write ("\t{0}\n".format(str(record.sequence[(PositionA-1):PositionB])))	
							fOFEN.write ("\n")
							j+=1		# Counter j for Nontarget protein counting 
							# Testing
							print "Save One"
		fOFE.write ("\n")		
		fOFE.write ("Total "+str(i)+"Found")
		fOFEN.write ("\n")		
		fOFEN.write ("Total "+str(j)+"Found")
		"""
		print "ModuleTestGlobalStatBeforeGlobal"
		print GlobalStat					
		"""
		global GlobalStatTarget
		global GlobalStatNonTarget
		GlobalStatTarget = i
		GlobalStatNonTarget = j
		print "ModuleTestGlobalStat"
		print GlobalStatTarget					
		print "ModuleTestGlobalStat"
		print GlobalStatNonTarget					
		"""
						for listee in FeatureList
						PositionA = listee[1]
						PositionB = listee[2]
						fOFE.write ("\t{0}\n".format(listee))
						fOFE.write ("\t{0}\n".format(str(record.sequence[(PositionA-1):PositionB])))	
						fOFE.write ("\n")
		"""

		"""
				if ("Cyto" in listee) or ("cyto" in listee) :
					PositionA = listee[1]
					PositionB = listee[2]
					if (record.sequence[(PositionA-1):PositionB] == str(TargetSeq)):				
						fOFC.write (">{0}\n".format(record.accessions))
						fOFC.write ("\t{0}\n".format(record.entry_name))
						fOFC.write ("\t{0}\n".format(listee))
						fOFC.write ("\t{0}\n".format(str(record.sequence[(PositionA-1):PositionB])))	
						fOFC.write ("\n")
						j+=1				

						
						for listee in FeatureList:
							PositionA = listee[1]
							PositionB = listee[2]
							fOFC.write ("\t{0}\n".format(listee))
							fOFC.write ("\t{0}\n".format(str(record.sequence[(PositionA-1):PositionB])))	
							fOFC.write ("\n")
						
				if ("Mito" in listee) or ("mito" in listee) :
					PositionA = listee[1]
					PositionB = listee[2]
					if (record.sequence[(PositionA-1):PositionB] == str(TargetSeq)):				
						fOFM.write (">{0}\n".format(record.accessions))
						fOFM.write ("\t{0}\n".format(record.entry_name))
						fOFM.write ("\t{0}\n".format(listee))
						fOFM.write ("\t{0}\n".format(str(record.sequence[(PositionA-1):PositionB])))	
						fOFM.write ("\n")
						k+=1

							
						for listee in FeatureList
							PositionA = listee[1]
							PositionB = listee[2]
							fOFM.write ("\t{0}\n".format(listee))
							fOFM.write ("\t{0}\n".format(str(record.sequence[(PositionA-1):PositionB])))	
							fOFM.write ("\n")
						
		
						
							elif ("PEPTIDE" in listee) or ("PROPEP" in listee) or ("SIGNAL" in listee):
								fOFP.write (">{0}\n".format(accession.id))
								ProcessedPepWrite(FeatureList,fOFP,accession,record)
								break
							elif ("CHAIN" in listee):
								DummyCounter=0
								for listeeDummy in FeatureList:
									if not (("PEPTIDE" in listeeDummy) or ("PROPEP" in listeeDummy) or ("SIGNAL" in listeeDummy)):
										DummyCounter+=1
								if DummyCounter == len(FeatureList):	
									fOFC.write (">{0}\n".format(accession.id))
									PositionA = listee[1] 
									PositionB = listee[2]
									if (isinstance(PositionA,int) and not (isinstance(PositionB,int))):
										PositionB = record.sequence_length
									else:
										PositionA = 1 
										PositionB = record.sequence_length				

									# Testing 
									print listee
									print PositionB

									WriteF (fOFC,accession,listee,record,PositionA,PositionB)
								break
						
		"""
