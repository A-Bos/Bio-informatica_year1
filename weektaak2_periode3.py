## author: Amber Bos
#  date / last date: 11-02-2020 / 11-02-2020
#  function:    reading 1 humane chromosome, 1 plant chromosoom, 2 bacteria chromosoom.fasta
#               Ursus arctos (Brown Bear), Escherichia coli (bacteria), Clostridium botulinum (bacteria),
#               Microcystis aeruginosa (Blue-green algae).
#               GC% plot:
#               - average GC%
#               - variation GC% and median
#               - GC% per 100bp
#  version:     1.0

def Ursus_arctos(Ua):
    with open(Ua) as doc:
        Ua_header = doc.readline()
        Ua_seq = doc.readlines()
        Ua_seq = "".join(Ua_seq).replace("\n","")
        Ua_seq = Ua_seq.split()
        cnt = 1
        while Ua_seq:
            linedoc_seq = Ua_seq.readlist()
            linedoc_GC = 100/len(linedoc_seq)*(linedoc_seq.count(c)+linedoc_seq.count(g))
        line = linedoc.readline()
        cnt += 1
        return linedoc_GC

#def Escherichia_coli(Ec):
   # with open(Ec) as doc:
    #    Ec_header = doc.readline()
     #   Ec_seq = doc.readlines()
      #  Ec_seq = "".join(seq).replace("\n","")
       # Ec_GC_av = 100/len(Ec_seq)*(Ec_seq.count(c)+Ec_seq.count(g))
    pass
    
#def Clostridium_botulium(Cb):
   # with open(Cb) as doc:
    #    Cb_header = doc.readline()
     #   Cb_seq = doc.readlines()
      #  Cb_seq = "".join(seq).replace("\n","")
       # Cb_GC_av = 100/len(Cb_seq)*(Cb_seq.count(c)+Cb_seq.count(g))
    pass

#def Microcystis_aeruginosa(Ma):
   # with open(Ua) as doc:
    #    Ma_header = doc.readline()
     #   Ma_seq = doc.readlines()
      #  Ma_seq = "".join(seq).replace("\n","")
       # Ma_GC_av = 100/len(Ma_seq)*(Ma_seq.count(c)+Ma_seq.count(g))
    pass

def main():

    Ua = "Ursus_arctos_genome.fasta"
    Ec = "Escherichia_coli_IAI39_genome.fasta"
    Cb = "Clostridium_botulinum_genome.fasta"
    Ma = "Microcystis_aeruginosa_genome.fasta"
    linedoc_GC = Ursus_arctos(Ua)
    print (linedoc_GC)

c = "C"
g = "G"
main()
