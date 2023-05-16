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
