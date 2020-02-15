# Author: 	Amber Bos	
# Date: 	11-11-2019
# Version: 	1
# Function: 	reading document fasta format;
#		is it DNA?;
#		does the enzym cut?

def content(document):
    with open(document) as doc:
        header = doc.readline()
        seq = doc.readlines()
        seq = "".join(seq).replace("\n","")
    return header, seq

def dna(seq):
    a = "A"
    c = "C"
    t = "T"
    g = "G"
    h = "H"
    total_length = len(seq)
    actgh = seq.count(a)+seq.count(c)+seq.count(t)+seq.count(g)+seq.count(h)
    if total_length == actgh:
        print(seq)
        print("It is DNA")
        return True
    else:
        print(seq)
        print("It isn/'t DNA")
        return False
    

def cut(seq):
    DdeI   = "CTGAG"    
    BspMII = "TCCGGA"  
    EcoRI  = "GAATTC"   
    HindIII= "AAGCTT"  
    TaqI   = "TCGA"
    DdeI_cut = seq.find("CTGAG")
    if DdeI_cut >= 0:
        print ("DdeI does cut.")
        print ("Place: ",seq.index("CTGAG"))
    else:
        print ("DdeI does not cut.")
    BspMII_cut = seq.find("TCCGGA")
    if BspMII_cut >= 0:
        print ("BspMII does cut.")
        print ("Place: ",seq.index("TCCGGA"))
    else:
        print ("BspMII does not cut.")
    EcoRI_cut = seq.find("GAATTC")
    if EcoRI_cut >= 0:
        print ("EcoRI does cut.")
        print ("Place: ",seq.index("GAATTC"))
    else:
        print ("EcoRI does not cut.")
    HindIII_cut = seq.find("AAGCTT")
    if HindIII_cut >= 0:
        print ("HindIII does cut.")
        print ("Place: ",seq.index("AAGCTT"))
    else:
        print ("HindIII does not cut.")
    TaqI_cut = seq.find("TCGA")
    if TaqI_cut >= 0:
        print ("TaqI does cut.")
        print ("Place: ",seq.index("TCGA"))
    else:
        print ("TaqI does not cut.")

def main():
    document = "lamaseq.fasta"
    header, seq = content(document)
    print(header)
    dna2 = dna(seq)
    if dna2 == True:
        cut(seq)
    elif dna2 == False:
        pass
    else:
        print("Error")
main()

