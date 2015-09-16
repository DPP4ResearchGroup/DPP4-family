#Loading Required Libraries
library(KEGGREST)

# Setting Working Directory
setwd("./")

Pathway = read.table ("FSortCode.txt")
PSize = nrow (Pathway)

for (i in 1:PSize) {
  path = Pathway [i,2]
  
  write (paste(paste(Pathway[i,1], Pathway[i,2], sep = "\t"), keggGet(path)[[1]]$NAME, sep = "\n"),file = "AFSortCode.txt",append=TRUE)
  write ("\n\n", file = "AFSortCode.txt",append=TRUE)
  
  # Testing Stability
  print ("Done One")
  flush.console()
}
