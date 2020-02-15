my_blast_db = '/Users/RobertQiao/Desktop/FlindersLab/BioThesis/Database/uniprot-organism-mouse.db'
my_blast_file = '/Users/RobertQiao/Desktop/FlindersLab/BioThesis/Database/uniprot-organism-human.fasta'
my_blast_exe = '/Users/RobertQiao/Desktop/FlindersLab/BioThesis/BlastExecutable/ncbi-blast-2.5.0+/bin/blastp'
humanfasta_file = '/Users/RobertQiao/Desktop/FlindersLab/BioThesis/Database/uniprot-organism-human.fasta'
mousefasta_file = '/Users/RobertQiao/Desktop/FlindersLab/BioThesis/Database/uniprot-organism-mouse.fasta'

#from Bio.Blast.Applications import NcbiblastpCommandline
#blastp_cline =  NcbiblastpCommandline (my_blast_exe, query = my_blast_file, db = my_blast_db, outfmt=5, out = "BlastResult.xml", max_hsps=5, num_threads=16)
#stdout, stderr = blastp_cline()
#print stdout,stderr

from Bio.Blast import NCBIXML
result_handle = open ("BlastResult.xml","rU")
blast_records = NCBIXML.parse (result_handle)

from Bio import SeqIO
# file organisation
hfile = open (humanfasta_file,"rU")
mfile = open (mousefasta_file,"rU")
wfile = open ("Match.txt","w")
statsfile = open ("Stats.txt","w")
hrecords = list( SeqIO.parse(hfile,"fasta"))
mrecords = list( SeqIO.parse(mfile,"fasta"))
hfile.close()
mfile.close()

# Counters
i = 0
CHECK = False
## Orphan Counters
Orphan = 0
NoMatch = 0

with wfile:
 with statsfile:

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
                       					Orphan += 1
						wfile.write ("\n")
						break
				else:
			 			wfile.write (str("no match" +  "\n"))
                        			NoMatch += 1
						continue
		else:
			wfile.write (str("no match" +  "\n"))
            		NoMatch += 1

		i += 1
		CHECK = False

    statsfile.write(str("Total") + "\t" + str("OrphanSeq") + "\t" + str("NoMatchSeq") + "\n")
    statsfile.write(str(i-1) + "\t" +str(Orphan) + "\t" + str(NoMatch) + "\n")
    print (str("Total") + "\t" + str("OrphanSeq") + "\t" + str("NoMatchSeq") + "\n")
    print (str(i-1) + "\t" +str(Orphan) + "\t" + str(NoMatch) + "\n")

 statsfile.close()
wfile.close()
