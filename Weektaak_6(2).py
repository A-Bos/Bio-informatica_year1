# Auteur: Amber Bos
# Last updated: 20-10-2019
# First: compair two sequences or information about one?
# Compair: two protains (= with one is longer and how are they the same?) one protain + one RNA (=how many times longer?)
# Information: is it RNA or protain? RNA (= GC%) protain (=load and mass).

print("Hello, I am build to help you out with your sequence.")
compair_q = input("Do you want information about one sequence or want to compair two? (1/2)")
if compair_q == "1":
    data = input("Put the sequence here: ")
    length = len(data)
    a = data.count("A")
    t = data.count("T")
    g = data.count("G")
    c = data.count("C")
    n = data.count("N")
    atgcn = a+t+g+c+n
    if atgcn == length:
        print("You have given me a RNA sequence.")
        print("Total A: ",a,"\n","Total T: ",t,"\n","Total G: ",g,"\n","Total C: ",c,"\n","Total N: ",n)
        print("Total length of the sequence: ", length)
        gc_q = input("Do you want to know the GC%? (y/n) ")
        if gc_q == "y":
            data = mRNA_organism
            name_organism = input("What is the name of the organism? ")
            GC_mRNA_organism = 100/len(mRNA_organism)*(mRNA_organism.count(c)+mRNA_organism.count(g))
            print ("The GC% for", name_organism, "is", GC_mRNA_organism)
        elif gc_q == "n":
            print("Alright.","\n","Quit.")
            quit
        else:
            print("I don't understand.", "\n", "Quit")
            quit
    else:
        print("You have given me a protain sequence.")
        d = data.count("D")
        e = data.count("E")
        r = data.count("R")
        k = data.count("K")
        print("Total D ",d,"\n","Total E ",e,"\n","Total R ",r,"\n","Total K ",k)
        print ("Total length of the sequence: ",length)
        if r+k > d+e:
            charge = "positive"
        elif r+k < d+e: 
            charge = "negative"
        else:
            charge = "neutral"
        print("This protain is ",charge," charged.")
        mass_q = input("Do you want to know the mass of the protain? (y/n)")
        if mass_q == "y":
            data = protain_organism
            a = 71.0788
            r = 156.1875
            n = 114.1038
            d = 115.0886
            c = 103.1388
            e = 129.1155
            q = 128.1307
            g = 57.0519
            h = 137.1411
            i = 113.1594
            l = 113.1594
            k = 128.1741
            m = 131.1926
            f = 147.1766
            p = 97.1167
            s = 87.0782
            t = 101.1051
            w = 186.2132
            y = 163.1760
            v = 99.1326
            A = protain_organism.count("A")
            R = protain_organism.count("R")
            N = protain_organism.count("N")
            D = protain_organism.count("D")
            C = protain_organism.count("C")
            E = protain_organism.count("E")
            Q = protain_organism.count("Q")
            G = protain_organism.count("G")
            H = protain_organism.count("H")
            I = protain_organism.count("I")
            L = protain_organism.count("L")
            K = protain_organism.count("K")
            M = protain_organism.count("M")
            F = protain_organism.count("F")
            P = protain_organism.count("P")
            S = protain_organism.count("S")
            T = protain_organism.count("T")
            W = protain_organism.count("W")
            Y = protain_organism.count("Y")
            V = protain_organism.count("V")
            mass_protain = (A*a)+(R*r)+(N*n)+(D*d)+(C*c)+(E*e)+(Q*q)+(G*g)+(H*h)+(I*i)+(L*l)+(K*k)+(M*m)+(F*f)+(P*p)+(S*s)+(T*t)+(W*w)+(Y*y)+(V*v)
            print("The mass of the protain is: ",mass_protain)
            quit
        elif mass_q == "n":
            print("Alright.","\n","Quit.")
            quit
        else:
            print("I don't understand.","\n","Quit.")
            quit
elif compair_q == "2":
    protain_RNA_q = input("Do you want to compair two protains or a protain and a RNA sequence? (2p/1p1r)")
    if protain_RNA-q == "2p": 
        protain_one = input("Put the first sequence here: ")
        protain_two = input("Put the second sequence here: ")
        len_one = len(protain_one)
        len_two = len(pritain_two)
        tel = 0
        print("Protain one is", len_one, "long.", "\n" + "Protain two is", len_two, "long.")
        if len_one < len_two:
                len_long = len_two
                len_small = len_one
        else:
                len_long = len_one
                len_small = len_two
        for place in range(len_small):
            if protain_one[place] == protain_two[place]:
                tel += 1
    elif protain_RNA_q == "1p1r":
        protain = input("Put the protain sequence here: ")
        RNA = input("Puth the RNA sequence here: ")
        length_RNA = len(RNA)
        length_protain = len(protain)
        print("The RNA sequence is "+str(length_RNA/length_protain)+" times bigger")
else:
    print("I don't understand.","\n","Quit.")
    quit
