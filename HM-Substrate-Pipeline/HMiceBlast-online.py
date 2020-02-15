from Bio.Blast import NCBIWWW
import os 

# help (NCBIWWW.qblast)

# Variables 
i = 1

# File Process 
file = open("Seq.csv","r")
for line in file:
	for words in line.split():

		seq = words 
		#"YAEGTFISDYSIAMDKIHQQDFVNWLLAQKGKKNDWKHNITQ"
		result_handle = NCBIWWW.qblast ("blastp", "swissprot", seq, entrez_query="Mus musculus[Organism]", expect = 0.1, format_type = "Text")


		# Pasing result_handle 
		blast_results = result_handle.read()
		filename = str(i)+".xml"
		# Write into a new directory 
		path = os.path.join("Blast",filename)
		with open (path,"w") as save_file:
			save_file.write(blast_results)
			print blast_results
		# Counter 
		i += 1
file.close()
