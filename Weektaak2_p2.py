## Aurthor: Amber Bos
## Date: 20-11-2019
## Function: --
## Version: 1.0



## 5'utr prokaryotes cuts at AGGAGGU
## 5'utr eukaryotes cuts at ACCAUGG

g = "G"
c = "C"
t = "T"
a = "A"
h = "H"

def content(document):
    with open(document) as doc:
        header = doc.readline()
        seq = doc.readlines()
        seq = "".join(seq).replace("\n","")
    return header, seq

def cds(seq):
    prokaryotes_cut = seq.find("AGGAGGU")
    eukaryotes_cut = seq.find("ACCAUGG")
    if prokaryotes_cut >= 0:
        print("5'UTR part has been found.")
        place = seq.index("AGGAGGU")
        if eukaryotes_cut >= 0:
            print("5'UTR part has been found.")
        elif eukaryotes_cut <= 0:
            print("5'UTR part has not been found.")
    elif prokaryotes_cut <= 0:
        print("5'UTR part had not been found.")
        if eukaryotes_cut >= 0:
            print("5'UTR part has been found.")
        elif eukaryotes_cut <= 0:
            print("5'UTR part has not been found.")
    else:
        print("Error finding 5'UTR part.")
        quit

def main():
    document =  "prpf4_mRNA.fasta"
    header, seq = content(document)
    cds(seq)
    length = len(seq)
    gc_perc = 100/len(seq)*(seq.count(g)+seq.count(c))
    meltingpoint = 4*(seq.count(g)+seq.count(c))+2*(seq.count(a)+seq.count(t))
    print("The length of the sequence is {}.".format(length))
    print("The GC% of the sequence is {}%.".format(gc_perc))
    print("The theoratical melting point is {}°C.".format(meltingpoint))
    

main()
    
    
