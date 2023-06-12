# ZADATAK: Napišite Python program unutar kojeg ćete kreirati rječnik koji sadrži barem 10 država Europe kao ključeve
# i njihove glavne gradove kao vrijednosti. 

# Program bi trebao izabrati slučajnu državu iz rječnika, pitati korisnika koji je glavni grad te države i 
# ispisati je li odgovor točan. 

# Program treba brojati točne odgovore. Kad korisnik pogriješi igra je završena i ispisan je broj točni odgovora.

import random

drzave = {
    "Albanija" : "Tirana",
    "Hrvatska" : "Zagreb",
    "Srbija": "Beograd",
    "Austrija": "Beč",
    "Crna Gora": "Podgorica"
}

broj_tocnih_odgovora = 0

kviz_traje = True

while kviz_traje:
    if len(drzave) == 0:
        print('Svaka čast, znao si sve glavne gradove!')
        kviz_traje = False
    else:
        slucajna_drzava = random.choice(list(drzave.keys()))

        glavni_grad = drzave[slucajna_drzava]
        drzave.pop(slucajna_drzava)

        odgovor = input(f'Koji je glavni grad države: {slucajna_drzava}?')

        if glavni_grad.lower() == odgovor.lower():
            print("Točno!")
            broj_tocnih_odgovora += 1
        else:
            print("Netočno!")
            print(f"\nIgra je završena! Skupio si {broj_tocnih_odgovora} točnih odgovora!")
            break
        

