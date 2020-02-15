#is het DNA of eiwit?
import time
invoer = input("Tell me, at what organism are we going to look? ")
seq = input("Give me the sequence without enters: ")
a = seq.count("A")
c = seq.count("C")
t = seq.count("T")
g = seq.count("G")
h = seq.count("H")
seq_tot = len(seq)
acgth = a+c+t+g+h
if seq_tot == acgth: #mRNA
    print ("You have told me a mRNA sequence.")
    print ("This sequence is",seq_tot,"long.")
else: #eiwit
    print ("You have given me a protain sequence.")
    print ("This sequence is",seq_tot,"long.")
    print ("Do you want to know the lading of",invoer,"?") #vertalen
    invoer2 = input("(y/n) : ")
    if invoer2 == "y":
        d = seq.count("D")
        e = seq.count("E")
        r = seq.count("R")
        k = seq.count("K")
        print("This sequence has",d,"D,",e,"E,",r,"R and",k,"K.")
    else:
        print ("Okay. Have a nice day.")
        quit
