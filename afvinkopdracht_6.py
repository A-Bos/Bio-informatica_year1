# Author:       Amber Bos
# Date:         11-11-2019
# Version:      1
# Function:     Read .txt with enzyms;
#               does or does not cut;
#               Where does it cut?
#               beautiful output thingy

dna = 'ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC'

def content():
    document = "enzymen.txt"
    with open(document) as doc:
        line = doc.readline()
        cnt = 1
        while line:
            enzym, seq = line.split()
            seq = seq.replace("^","")
            dna_cut = dna.find(seq)
            if dna_cut >=  0:
               print("{} does cut at position {}".format(enzym,dna.index(seq)))
               print(dna)
               position = dna.index(seq)
               whitespace = position*" "
               print("{}{}".format(whitespace,seq))
            elif dna_cut == -1:
               pass
            else:
                print("error")
            line = doc.readline()
            cnt += 1
content()
