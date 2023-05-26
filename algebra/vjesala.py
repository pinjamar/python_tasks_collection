# igra vjesala
# racunalo ce odabrati nasumicnu rijec iz rjecnika
# igrac poksuava pogoditi slova koja sadri ta rijec

# iskoristit cemo do sad nauceno: liste, rjecnici, if, while, for...

# upute: logika igre je takva da mi testiramo duzinu rijeci koju korisnik mora pogoditi
# ako pogodimo slovo maknut cemo ga iz rijeci koju pogadamo i tada se smanjuje duljina te rijeci
# ako promasimo smanjit ce nam se broj zivota / povecati broj pokusaja
# igra je gotova kad duzina rijeci postane 0 ili ostanemo bez zivota

import random
vjesalo = {
    0: '''
    +---+
    |   |
        |
        |
        | 
        |
    =====''',
    1: '''
    +---+
    |   |
    O   |
        |
        | 
        |
    =====''',
    2: '''
    +---+
    |   |
    O   |
    |   |
        | 
        |
    =====''',
    3: '''
    +---+
    |   |
    O   |
    |\  |
        | 
        |
    =====''',
    4: '''
    +---+
    |   |
    O   |
   /|\  |
        | 
        |
    =====''',
    5: '''
    +---+
    |   |
    O   |
   /|\  |
     \  | 
        |
    =====''',
    6: '''
    +---+
    |   |
    O   |
   /|\  |
   / \  | 
        |
    =====''',
}

print("Dobrodosli u igru vjesala")
print("-------------------------------")
print()

lista_rijeci = ["python"]

trazena_rijec = random.choice(lista_rijeci).upper()
print("Trazena rijec je slijedeceg oblika:", end=" ")
for x in trazena_rijec:
    print("_", end=" ")

print()
slova_rijeci = []

for x in trazena_rijec:
    if x not in slova_rijeci:
        slova_rijeci.append(x)

iskoristena_slova = []

pokusaj = 0

while pokusaj < 7 and len(slova_rijeci) > 0:
    print(f"Iskoristeni pokusaji: {pokusaj}")
    print(f"Iskoristio si sljedeca slova: {iskoristena_slova}")

    print(vjesalo[pokusaj])

    print("Trenutna rijec: ", end=" ")
    for slovo in trazena_rijec:
        if slovo in iskoristena_slova:
            print(slovo, end=" ")
        else:
            print("-", end=" ")
    print()
    slovo_igraca = input("Pogodi slovo: ").upper()
    print()

    if slovo_igraca not in iskoristena_slova:
        iskoristena_slova.append(slovo_igraca)
        if slovo in slova_rijeci:
            print("Uneseno slovo je u rijeci!")
            slova_rijeci.remove(slovo_igraca)
        else:
            print("Slovo nije u rijeci")
            pokusaj += 1
    else:
        print("Ovo slovo je vec uneseno. Pokusaj ponovno!")
