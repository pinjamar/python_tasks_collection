brojevi = []
for broj in range(101):
    brojevi.append(broj)

izdvojeni_brojevi = brojevi[20: (44+1): 6]  # od 20 do 46 svaki 6. broj
for i in izdvojeni_brojevi:
    print(i, end=" ")
print()

izdvojeni_brojevi = brojevi[20: 45]
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[20:]  # od 20og indexa do kraja
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[:45]  # od pocetka do 45og indexa
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[:]  # sve
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[-1]
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[-2]  # samo predzadnji
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[-2:]  # od predzadnjeg do kraja
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[: -2]  # do prezadnjeg
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[:: -1]  # do zadnjeg, korak -1
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[: -3: -1]  # [: -stop : -step]
print(izdvojeni_brojevi)
print()

izdvojeni_brojevi = brojevi[-3:: -1]  # [: -start : -step]
print(izdvojeni_brojevi)
