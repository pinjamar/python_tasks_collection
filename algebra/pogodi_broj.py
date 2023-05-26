# zadata: pogodi broj > napisi program koji ce ti omoguciti pogadjanje broja

import random  # ovo je paket

# randibt razlikuje se od range, ovdje je zadnji broj (100) ukljucen
zamisljeni_broj = random.randint(1, 100)
broj_pokusaja = 0
while True:
    # print("Zamisljeni broj:", zamisljeni_broj)
    odgovor = input("Pogodi broj od 1 do 100 koji sam zamislio: \t")
    broj_pokusaja += 1

    if int(odgovor) == zamisljeni_broj:
        print()
        print("ČESTITAM! To je broj koji sam zamislio")
        print(f"Za to ti je bilo potrebno {broj_pokusaja} pokusaja")
        print()
        break
    elif int(odgovor) < zamisljeni_broj:
        print(f"Zamisljeni broj je veci od {odgovor}")
    elif int(odgovor) > zamisljeni_broj:
        print(f"Zamisljeni broj je manji od {odgovor}")
