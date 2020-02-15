# author:           Amber Bos
# date / last date: 13-02-2020
# version:          1.0
# function:         error solving:
#                   - the document doesnt excist
#                   - the document doens't have the correct format
#                   - doesn't have the correct input

import doctest
    
def content(doc):
    document = open(doc)
    headers = []
    seqs = []
    seq = ""
    for line in document:
        line = line.strip()
        if ">" in line :
            if seq != "":
                seqs.append(seq)
                seq = ""
                headers.append(line)
            else:
                seq += line.strip()
                seqs.append(seq)
    return headers, seqs

    
def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a+t+c+g
    if total == len(seq):
        dna = True
    return dna


def cut(alpaca_seq):
    document = open("enzymen.txt")
    for line in document:
        name,seq=line.split(" ")
        seq = seq.strip().replace("^","")
        if seq in alpaca_seq:
            print(name, "cuts in the seqence.")

def main():
    document="GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"
    
    
    headers, seqs = content(document)
    search = input("Search: ")
    for i in range(len(headers)):
        if search in headers[i]:
            print("Header:",headers[i])
            check_is_dna = is_dna(seqs[i])
            if check_is_dna:
                print("The sequence is DNA")
                cut(seqs[i])
            else:
                print("The sequence is not DNA. Someting went wrong.")

main()

