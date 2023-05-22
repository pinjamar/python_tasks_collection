vozila = {
    1: [
        "Kamion", "Iveco", "OS 001 ZZ", 2015, 45000.00
    ],
    2: [
        "Kamion", "Iveco", "OS 002 ZZ", 2015, 47000.00
    ],
    3: [
        "Tegljac", "MAN", "RI 001 ZZ", 2018, 78000.00
    ],
    4: [
        "Tegljac", "MAN", "RI 002 ZZ", 2020, 97000.00
    ],
    5: [
        "Kombi", "Mercedes", "ST 001 ZZ", 2013, 12000.00
    ],
    6: [
        "Kombi", "Volkswagen", "ST 002 ZZ", 2021, 35000.00
    ],
    7: [
        "Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", 2010, 9000.00
    ],
    8: [
        "Dostavno vozilo", "Volkswagen", "ZG002 ZZ", 2010, 9300.00
    ]
}

### CLEAR###
print()
print("Ispis prije clear()")
for kljuc, vrijednost in vozila.items():
    print(kljuc, end="\t")
    for element in vrijednost:
        print(element, end="\t")
    print()
print()
