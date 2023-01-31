tekst = "Dag iedereen"
lijst_tekens = []
for teken in tekst:
    ascii_nummer = (ord(teken))
    #bin_waarde = bin(ascii_nummer)
    #lijst_tekens.append(bin_waarde)
    lijst_tekens.append(ascii_nummer)
for getal in lijst_tekens:
    print(getal,end=" ")


