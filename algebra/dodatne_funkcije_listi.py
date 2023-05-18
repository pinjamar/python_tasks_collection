brojevi = []
for broj in range(21):
    brojevi.append(broj)

print()
print("Ispis cijele liste")
for i in brojevi:
    print(i, end=' ')
print("\n")

### CLEAR###
# brojevi.clear()
# print("Ispis nakon CLEAR()")
# for i in brojevi:
#     print(i, end=' ')
# print("\n")

### COPY   ###
brojevi_kopija = brojevi.copy()
print("Ispis nakon COPY()")
for i in brojevi_kopija:
    print(i, end=' ')
print("\n")

### COUNT  ###
brojevi_count = brojevi.count(15)
print(f"Broj pojavljivanja broja 15 u listi je: {brojevi_count}")
print("\n")

### EXTEND ###
rijeci = ["Python", "Programming", "Algebra"]
print("Ispis rijeci prije EXTEND:")
for i in rijeci:
    print(i, end=" ")
print("\n")

print("Brojevi prije extend:")
for i in brojevi:
    print(i, end=" ")
print("\n")

brojevi.extend(rijeci)
print("Brojevi nakon extend")
for i in brojevi:
    print(i, end=" ")
print("\n")

### index ###
brojevi_index = brojevi.index(15)
print("Indeks prvog pojavljivanja broja 15 u listi je", brojevi_index)
print(f"Vrijednost u listi brojevi na indeksu 15 je {brojevi[brojevi_index]}")
print()

### INSERT###
print("Ispis liste brojevi PRIJE insert() naredbe")
for broj in brojevi:
    print(broj, end=" ")
print()
brojevi.insert(15, "Ispred 15-ice")
print("Ispis liste brojevi NAKON insert() naredbe")
for broj in brojevi:
    print(i, end=" ")
    print("\n")

### REVERSE###
print("Ispis brojevi PRIJE reverse():")
for i in brojevi:
    print(i, end=" ")
print("\n")

brojevi.reverse()
print("Ispis brojevi NAKON reverse():")
for i in brojevi:
    print(i, end=" ")
print("\n")

### SORT###
rijeci = ["python", "program", "ruby", "java"]
print("Ispis rijeci prije sort():")
for rijec in rijeci:
    print(rijec, end=" ")
print("\n")

rijeci.sort()
print("Ispis rijeci nakon sort():")
for rijec in rijeci:
    print(rijec, end=" ")
print("\n")

rijeci.sort(reverse=True)  # sortiraj obrnuto
print("Ispis rijeci nakon sort(reverse):")
for rijec in rijeci:
    print(rijec, end=" ")
print("\n")
