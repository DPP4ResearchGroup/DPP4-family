# This module is used for seperate UniProt seqs into fragments accroding to the annotation info 

# Functions included in this module 

# Main seperation() function 
def seperation (records,OutFile):
    with open (OutFile, "w") as fw:
	for record in records:
		Keywords = list(record.keywords)
		Features = list(record.features)
		# Testing	
	        # print Keywords
		# print Features

		for feature in Features: 
			for element in feature:
				if ("PEPTIDE" in str(element)) or ("CHAIN" in str(element)):
					posA = (feature[1])
					posB = (feature[2])
					print feature
					if (str(feature[2]).find("?")!=-1):
						posB = record.sequence_length
						# Write files
					fw.write("{0}\t{1}\t{2}\n".format(record.accessions,record.entry_name,(record.sequence[(posA-1):posB])))
						
	
