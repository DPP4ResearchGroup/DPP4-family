source("http://bioconductor.org/biocLite.R")
biocLite()

#install.packages("wget")
#biocLite("PAnnBuilder")
#library(PAnnBuilder)
#getALLUrl("Homo sapiens")
#getALLBuilt("Homo sapiens") ## Get version/release
#biocLite("org.Hs.sp.db")

# Peptide calculation 
biocLite("Peptides")
library(Peptides)

# Prepare Sequences Mouse and Human
Mouse <- read.csv2(file="Excel/MouseFinalList.txt",sep = "\t",head=TRUE,as.is=TRUE)
Human <- read.csv2(file="Excel//HumanFinalList.txt",sep="\t",head=TRUE,as.is=TRUE)
MSeq = Mouse[,"SEQ"]
HSeq = Human [,"SEQ"]

# This part calculate MW of peptides before and after DPP4 digestion 
MFullLength = lapply(1:length(MSeq), function(x) {
  toString(MSeq[x])
})
MDPP4CleaveLength = lapply(1:length(MSeq),function(x) {
  substr(MSeq[x],3,nchar(MSeq[x]))
})
HFullLength = lapply(1:length(HSeq), function(x) {
  toString(HSeq[x])
})
HDPP4CleaveLength = lapply(1:length(HSeq),function(x) {
  substr(HSeq[x],3,nchar(HSeq[x]))
})
# Mouse MW
MMW<-lapply(1:length(MSeq),function(i){
  mw (MFullLength[i])
}) 
# Cleaved Mouse MW
MMWCleaved <- lapply(1:length(MSeq),function(i){
  mw (MDPP4CleaveLength[i])
})
MCleaved <- mapply('-',MMW,MMWCleaved,SIMPLIFY=FALSE)

# Human MW
HMW <- lapply(1:length(HSeq),function(i){
  mw (HFullLength[i])
})
HMWCleaved <- lapply(1:length(HSeq),function(i){
  mw (HDPP4CleaveLength[i])
})
HCleaved <- mapply('-',HMW,HMWCleaved,SIMPLIFY=FALSE)

# Append MW info to Mouse data.frame 
Mouse$MW <- unlist(MMW)
Mouse$AfterCleavageMW <- unlist(MMWCleaved)
Mouse$CleavedMW <- unlist(MCleaved)
# Append MW into Human data.frame
Human$MW <- unlist(HMW)
Human$AfterCleavageMW <- unlist(HMWCleaved)
Human$CleavedMW <- unlist (HCleaved)


# Save data into Master.csv file 
#install.packages("rjson")
#library(rjson)
Mouse$ID[Mouse$ID==""] <- "As ABOVE"
Mouse$SEQ=sapply(Mouse$SEQ,as.character)
write.table(data.frame(Mouse), file="MouseMaster.csv", append=FALSE, sep = "\t", eol="\n", na = "AS ABOVE", dec=".", row.names=FALSE, col.names=TRUE, qmethod="double")
# write.table(Mouse, file="Master.csv")
# write.csv(Mouse,file="Master.csv")
Human$ID[Human$ID==""] <- "As ABOVE"
Human$SEQ=sapply(Human$SEQ,as.character)
write.table(data.frame(Mouse), file="HumanMaster.csv", append=FALSE, sep = "\t", eol="\n", na = "AS ABOVE", dec=".", row.names=FALSE, col.names=TRUE, qmethod="double")


# Using Pairwise Sequence Alignment to Align similar Human and Mouse Proteins. 
biocLite("Biostrings")
library(Biostrings)
Align<-lapply(1:length(MSeq), function(i){
  pairwiseAlignment (pattern=HSeq,subject=MSeq[i])
})

# Using prealignment info 
biocLite("hom.Hs.inp.db")
library("hom.Hs.inp.db")
as.list(hom.Hs.inpMUSMU)
# Convert UniProt to ENSEMBLPROT
biocLite("rJava")
biocLite("IdMappingRetrieval")
library(IdMappingRetrieval)



# Defind a range for all the possible MW positive hit 
RangeTarget = lapply (1:length(Mouse$AfterCleavageMW), function(i){
  range(Mouse$AfterCleavageMW[i]-25,Mouse$AfterCleavageMW[i]+1)
})
Targetfile = read.csv("Excel//WT_1.csv",head=TRUE,as.is=TRUE)
mz = Targetfile$m.z
MassTest = lapply(1:length(mz), function(i){
  InternalTest = lapply(1:length(RangeTarget),function(x) {
     #if (mz[i]>Mouse$AfterCleavageMW[x]-2 & mz[i]<Mouse$AfterCleavageMW[x]+2) {
    findInterval(mz[1],unlist(RangeTarget[x])) 
  })
  return (1%in%InternalTest)
})
MassTest