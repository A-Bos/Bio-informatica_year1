# Iteratie opdracht
# Start script voor opgave over sikkelcel
# (c) Martijn van der Bruggen, 2007-2010
# Updates:
# November 2010, code bijgewerkt met instructies voor de opdracht
# Hogeschool van Arnhem en Nijmegen

# Sequenties voor respectievelijk sikkelcel- en normale cellen
# Bekend is dat het gen coderend voor hemoglobine bij sikkelcel aandoening een andere nucleotide heeft
# De sequentie voor de sikkelcel en een "gezonde bloedcel" zijn hier onder gegeven
sikkel_seq = 'GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'
normaal_seq ='GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'

# In het bestand enzymen. txt staan kandidaat restrictie enzymen
# Opdracht schrijf een programma dat al deze enzymen doorloopt, een suggestie
# geeft welk restrictie enzym welk knipt in de ene sequentie en niet in de andere sequentie
# Hiermee kunnen we diagnostisch enzym voorstellen om vast te stellen of een persoon
# drager is van het sikkelcel allel

###Author:      Amber Bos
###Date:        10-11-2019
###Function:    Reading document with enzymes;
###             does or doesn't cut at
###             normal and sickel cel.

def main():
    document = "enzymen.txt"
    with open(document) as doc:
       line = doc.readline()
       cnt = 1
       while line:
           enzym, seq = line.split()
           seq = seq.replace("^","")
           normaal_cut = normaal_seq.find(seq)
           sikkel_cut = sikkel_seq.find(seq)
           if normaal_cut >= 0:
               print("Normal cell: {} does cut at {}.".format(enzym,normaal_seq.index(seq)))
               if sikkel_cut >= 0:
                   print("Sickle cell: {} does also cut at {}.".format(enzym,sikkel_seq.index(seq)))
               else:
                   print("Sickle cell: {} does not cut.".format(enzym))
           else:
               print("Normal cell:{} does not cut.".format(enzym))
               if sikkel_cut >= 0:
                   print("Sickle cell: {} does also cut at {}.".format(enzym,sikkel_seq.index(seq)))
               else:
                   print("Sickle cell:{} does not cut.".format(enzym))
           line = doc.readline()
           cnt += 1
main()

    

# Aanwijzingen voor het schrijven van je programma
# -------------------------------------------------------------
# Het lezen van een regel kan met bestand.readline()
# Lees door totdat je een lege regel aantreft
# Een regel bestaat uit twee stukken: enzym en knipsequentie. Bijvoorbeeld: DdeI C^TGAG
# Het opsplitsen van een regel in twee stukken op de spatie kan middels: enzym, seq = regel.split()
# Door bovenstaande split verkrijg je twee variabelen enzym en seq, respectievelijk de naam van het enzym en de sequentie waar deze in knipt
# Verwijderen het dakje uit de seq met seq.replace("^","")
# --------------------------------------------------------------------

