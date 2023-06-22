### KAMEN ŠKARE PAPIR ###

# ZADATAK: Napravite program koji će vam omogućiti igrati kamen, škare, papir protiv računala

import random

# 1 -> Kamen
# 2 -> Škare
# 3 -> Papir

# while True:

#     izbor_racunala = random.randint(1, 3)
#     izbor_korisnika = int(input('Izaberite: kamen, škare ili papir:\t'))

#     if izbor_korisnika == izbor_racunala:
#         print('NERIJEŠENO! Izabrali ste isto kao i računalo')
#     elif izbor_korisnika == 1 and izbor_racunala == 3:
#         print('Izgubili ste, računalo je odabralo papir')
#     elif izbor_korisnika == 1 and izbor_racunala == 2:
#         print('POBIJEDILI STE, računalo je odabralo škare')
#     elif izbor_korisnika == 3 and izbor_racunala == 2:
#         print('Izgubili ste, računalo je odabralo škare')
#     elif izbor_korisnika == 3 and izbor_racunala == 1:
#         print('POBIJEDILI STE, računalo je odabralo kamen')
#     elif izbor_korisnika == 2 and izbor_racunala == 1:
#         print('Izgubili ste, računalo je odabralo kamen')
#     elif izbor_korisnika == 2 and izbor_racunala == 3:
#         print('POBIJEDILI STE, računalo je odabralo papir')
    
#     nastavak_igre = input('Želite li nastaviti igrati? Upišite NE za prestanak!').upper()
#     if nastavak_igre == 'NE':
#         break
#     else:
#         continue

def slucajni_izbor():
    return random.randint(1, 3)

def provjera_ishoda_igre(izbor_racunala, izbor_korisnika):
    if izbor_korisnika == izbor_racunala:
        print('NERIJEŠENO! Izabrali ste isto kao i računalo')
    elif izbor_korisnika == 1 and izbor_racunala == 3:
        print('Izgubili ste, računalo je odabralo papir')
    elif izbor_korisnika == 1 and izbor_racunala == 2:
        print('POBIJEDILI STE, računalo je odabralo škare')
    elif izbor_korisnika == 3 and izbor_racunala == 2:
        print('Izgubili ste, računalo je odabralo škare')
    elif izbor_korisnika == 3 and izbor_racunala == 1:
        print('POBIJEDILI STE, računalo je odabralo kamen')
    elif izbor_korisnika == 2 and izbor_racunala == 1:
        print('Izgubili ste, računalo je odabralo kamen')
    elif izbor_korisnika == 2 and izbor_racunala == 3:
        print('POBIJEDILI STE, računalo je odabralo papir')

def kamen_skare_papir():
    game_on = True
    while game_on:

        izbor_racunala = random.randint(1, 3)

        izbor_korisnika = int(input('Izaberite: kamen, škare ili papir:\t'))

        provjera_ishoda_igre(izbor_racunala, izbor_korisnika)
        
        nastavak_igre = input('Želite li nastaviti igrati? Upišite NE za prestanak!').upper()
        if nastavak_igre == 'NE':
            game_on = False
        else:
            game_on = True

# kamen_skare_papir()

provjera_ishoda_igre(1, 2)