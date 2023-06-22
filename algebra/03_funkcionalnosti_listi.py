brojevi = []
# print(brojevi)
print("Unos brojeva u listu")
for broj in range(100):
    print(broj, end=" ")
    brojevi.append(broj)

print()
print()

# print(brojevi)

for broj in brojevi:
    print(broj, end=" ")

print()
print()

########################################################################
brojevi = []
for broj in range(1, 50, 2):
    brojevi.append(broj)

broj_elemenata = len(brojevi)

print(f"Broj elemenata liste je: {broj_elemenata}")

### PROSJEK BROJEVA U LISTI###

brojevi = []

for broj in range(1, 45):
    brojevi.append(broj)


### pjeske###
zbroj = 0
for element in brojevi:
    # zbroj = zbroj + element # postoji i bolji nacin
    zbroj += element

broj_elemenata = len(brojevi)
prosjek = zbroj / broj_elemenata

print(f"Prosjek elemenata je: {prosjek}")
print()

### Elegantniji nacin###
prosjek_elemenata = sum(brojevi) / len(brojevi)
print(f"Prosjek elemenata je: {prosjek_elemenata}")
print()

### Jos elegantnije###
print(f"Prosjek elemenata liste je: {sum(brojevi) / len(brojevi)}")


### izmjena elemenata liste###

zadaci = [
    "odabrati naziv liste",
    "unijeti elemente liste",
    "pokrenuti aktivnosti nad listom"
]

indeks = 0
for zadatak in zadaci:
    print(f'{indeks}. element liste "zadaci": {zadatak}')
    indeks += 1
print()

# zelimo izmjeniti drugi element liste zadaci
zadaci[1] = "Drugi element liste zadaci"
print(zadaci)
