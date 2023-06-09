# Igra vješala
# Računalo će odabrati nasumičnu riječ iz rječnika
# Igrač pokušava pogoditi slova koja sadrži ta riječ

# Iskoristit ćemo do sad naučeno: liste, rječnici, if, while, for...

# UPUTE: Logika igre je takva da mi testiramo dužinu riječi koju korisnik mora pogoditi.
# Ako pogodimo slovo maknut ćemo ga iz riječi koju pogađamo i tada se smanjuje duljina te riječi, 
# ako promašimo smanjit će nam se broj života / povećati broj pokušaja
# Igra je gotova kad dužina riječi postane 0 ili ostanemo bez života!!

import random

vjesalo = {
    0:'''
    +---+
    |   |
        |
        |
        |
        |
    ======''',
    1:'''
    +---+
    |   |
    O   |
        |
        |
        |
    ======''',
    2:'''
    +---+
    |   |
    O   |
    |   |
        |
        |
    ======''',
    3:'''
    +---+
    |   |
    O   |
    |   |
   /    |
        |
    ======''',
    4:'''
    +---+
    |   |
    O   |
    |   |
   / \  |
        |
    ======''',
    5:'''
    +---+
    |   |
    O   |
    |   |
   /|\  |
        |
    ======''',
    6:'''
    +---+
    |   |
    O   |
    |   |
   /|\  |
   /    |
    ======''',
    7:'''
    +---+
    |   |
    O   |
    |   |
   /|\  |
   / \  |
    ======'''
}

def isprintaj_vjesala(zivot):
    print(vjesalo[zivot])

lista_rijeci = ['Python', 'Algebra', 'Programiranje', 'jabuka', 'AuToMoBIL'] 

def odaberi_slucajnu_rijec():
    slucajna_rijec = random.choice(lista_rijeci).upper()
    print('Ispis is odaber_slucajnu_rijec funkcije')
    print(slucajna_rijec)
    return slucajna_rijec
    # return trazena_rijec

def vjesala():

    trazena_rijec = odaberi_slucajnu_rijec()
    print('Print iz vjesala()')
    print(trazena_rijec)

    for x in trazena_rijec:
        print(x)
    
    isprintaj_vjesala(5)

vjesala()

