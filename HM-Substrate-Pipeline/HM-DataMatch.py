my_blast_db = '/Users/RobertQiao/Desktop/FlindersLab/BioThesis/Database/Mouse.db'
my_blast_file = '/Users/RobertQiao/Desktop/FlindersLab/BioThesis/Human.fasta'
my_blast_exe = '/Users/RobertQiao/Desktop/FlindersLab/BioThesis/BlastExecutable/ncbi-blast-2.5.0+/bin/blastp'

from Bio.Blast.Applications import NcbiblastpCommandline
blastp_cline =  NcbiblastpCommandline (my_blast_exe, query = my_blast_file, db = my_blast_db, outfmt=5, out = "BlastResult.xml", max_hsps=5, num_threads=2)
stdout, stderr = blastp_cline()
print stdout,stderr

from Bio.Blast import NCBIXML 
result_handle = open ("BlastResult.xml","rU")
blast_records = NCBIXML.parse (result_handle) 

from Bio import SeqIO
# file organisation 
hfile = open ("Human.fasta","rU")
mfile = open ("Mouse.fasta","rU")
wfile = open ("Match.txt","w")
hrecords = list( SeqIO.parse(hfile,"fasta"))
mrecords = list( SeqIO.parse(mfile,"fasta"))
hfile.close()
mfile.close()

i = 0
CHECK = False

with wfile: 	
 
    for blast_record in blast_records:
		
		hrecord =  hrecords [i]
		print  hrecord.description	
		wfile.write (str(hrecord.description + '\t' + hrecord.seq + '\t'))  	
	
		if (blast_record.alignments):
			alignment = blast_record.alignments [0]
	
			for hsp in alignment.hsps:
						
				if ((len(hsp.query) < 20) & (hsp.score > 18)) or ((len(hsp.query) >= 20) & (hsp.score > 20 * len(hsp.query)/20.0)): 
				
						for mrecord in mrecords:
							if mrecord.seq == hsp.sbjct: 	
								wfile.write (str(mrecord.description + "\t" + mrecord.seq + "\t"))
								CHECK = True
						if (CHECK == False):
							wfile.write (str("NO MOUSE SEQ!"))
						wfile.write ("\n")
						break		
				else: 
			 			wfile.write (str("no match" +  "\n"))
						continue
		else: 
			wfile.write (str("no match" +  "\n"))
		i += 1 
		CHECK = False
	
wfile.close()
