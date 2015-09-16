#Loading Required Libraries
source("https://bioconductor.org/biocLite.R")
biocLite("KEGGREST")
library(KEGGREST)

# Setting Working Directory
setwd("./")

UniProt = read.table ("RInput.dat")
RInputSize = nrow (UniProt)

for (i in 1:RInputSize) {
  # Testing 
  # print (i)
  
  uniprotID = UniProt[i,1]
  # Stability Testing 
  # print (uniprotID)
  
  # 1st Conversion to hsa (HUMAN genes)
  spID = paste ("sp:",UniProt[i,1],sep="") 
  hsaID = keggConv("genes",as.character(spID))
  # Testing Stability 
  # print (spID)
  # print (hsaID)
  
  # 2nd Conversion to Human gene related Disease
  if (length(hsaID)!=0L) {
    if (length(keggGet(hsaID))!=0L){
      # Testing Stability 
      print (length(names(keggGet(hsaID)[[1]]$PATHWAY)))
      
      if ((length(names(keggGet(hsaID)[[1]]$PATHWAY))!=0) & (is.null(keggGet(hsaID)[[1]]$PATHWAY)==FALSE)){
        # Testing Stability 
        print ("Done Step One") 
        for (m in 1:length(names(keggGet(hsaID)[[1]]$PATHWAY))) {
          write (paste(paste(spID,names(keggGet(hsaID)[[1]]$PATHWAY[m]),sep="\n"),keggGet(names(keggGet(hsaID)[[1]]$PATHWAY[m]))[[1]]$NAME,sep="\n"),file="Pathway.txt", append=TRUE)}
        write ("\n\n",file="Pathway.txt",append=TRUE)
        # Testing Stability 
        print ("Done Step Two")        
        
#        # 3rd Conversion into Cancer, Judge whether cancer is consequence
#       CancerIndex = read.table("CancerH.txt")
#         
#         for (k in 1:length(names(keggGet(hsaID)[[1]]$DISEASE))) {
#           # Testing k
#           print (paste("k=",k))
#           for (j in 1:nrow(CancerIndex)) {
#             # Testing j
#             print (paste("j=",j))
#             if (names(keggGet(hsaID)[[1]]$DISEASE[k])==CancerIndex[j,1]) {
#               write (paste(paste(spID,names(keggGet(hsaID)[[1]]$DISEASE[k]),sep="\n"),keggGet(CancerIndex[j,1])[[1]]$DESCRIPTION,sep="\n"),file="CancerSubstrates.txt", append=TRUE)
#               write ("\n\n",file="CancerSubstrates.txt",append=TRUE)
#               # Stability Testing
#               print ("Found one!")
#             } 
#           } 
#         } 
      }
      flush.console()
    }
  }
}


