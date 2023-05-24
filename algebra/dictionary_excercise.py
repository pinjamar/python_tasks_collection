# koristeci rjecnik koji je definiran nize napisite program koji ce dati odgovor na slijedeca pitanja

# 1. Koji klubovi se smatraju top 6 klubovima u Premiershipu?
# 2. Koliko iznosi broj najviše osvojenih titula jednog kluba?
# 3. Koliko iznosi najmanji broj osvojenih titula jednog kluba?
# 4. Tko je kapetan Arsenala?
# 5. Tko je trener Manchester Cityja?
# 6. Na kojem stadionu igra Liverpool?
# 7. Tko je osvojio najviše titula?
# 8. Tko je osvojio najmanje titula?


eng_top6_klubovi = {

    "Manchester City": {
        "titule": 7,
        "trener": "Pep Guardiola",
        "kapetan": "Kevin De Bruyne",
        "stadion": "Etihad"
    },
    "Manchester United": {
        "titule": 13,
        "trener": "Erik Ten Hag",
        "kapetan": "Bruno Fernandes",
        "stadion": "Old Trafford"
    },
    "Liverpool": {
        "titule": 1,
        "trener": "Jurgen Klopp",
        "kapetan": "Mohamed Salah",
        "stadion": "Anfield"
    },
    "Tottenham": {
        "titule": 0,
        "trener": "Christian Stellini",
        "kapetan": "Harry Kane",
        "stadion": "White Hart Lane"
    },
    "Arsenal": {
        "titule": 3,
        "trener": "Mikel Arteta",
        "kapetan": "Martin Odegaard",
        "stadion": "Emirates"
    },
    "Chelsea": {
        "titule": 5,
        "trener": "Frank Lampard",
        "kapetan": "Cezar Azpilicueta",
        "stadion": "Stamford Bridge"
    }
}

# 1. Koji klubovi se smatraju top 6 klubovima u Premiershipu?

# for key in eng_top6_klubovi.keys():
#     print("\t", key)
# print()

top_klubovi = []
for key in eng_top6_klubovi.keys():
    top_klubovi.append(key)

for key in eng_top6_klubovi.keys():
    if key != top_klubovi[-1]:
        print(key, end=', ')
    else:
        print(key, end='. ')
print()

# 2. Koliko iznosi broj najviše osvojenih titula jednog kluba?

broj_titula = []
kapetani_momcadi = []
for key, value in eng_top6_klubovi.items():
    broj_titula.append(value["titule"])
    kapetani_momcadi.append(value["kapetan"])

# print(broj_titula)
# print(kapetani_momcadi)
print(f"Broj najvise osvojenih titula je: {max(broj_titula)}")
print(f"Broj najmanje osvojenih titula je: {min(broj_titula)}")


# Odgovor na 4, 5 i 6 pitanje
print(eng_top6_klubovi["Arsenal"]["kapetan"])
print(f"Kapetan Arsenala je: {eng_top6_klubovi['Arsenal']['kapetan']}")
print(f"Trener Chelsea je: {eng_top6_klubovi['Chelsea']['trener']}")
print(f"Liverpoolov stadion je: {eng_top6_klubovi['Liverpool']['stadion']}")

# Odgovor na 7 i 8 pitanje
broj_titula = []
for key, value in eng_top6_klubovi.items():
    broj_titula.append(value['titule'])

print(broj_titula)

for key, value in eng_top6_klubovi.items():
    if value['titule'] == max(broj_titula):
        print(f"Klub koji je osvojio najvise titula je: {key}")
    if value['titule'] == min(broj_titula):
        print(f"Klub koji je osvojio najmanje titula je: {key}")
    if value['trener'] == "Frank Lampard":
        print(f"Frank Lampard trenira: {key}")
