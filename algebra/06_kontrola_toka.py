# IF petlja kao i FOR ima svoj blok instrukcija pa onda na kraju dolazi : znak.
# Primjer

prvi_uvjet = True
drugi_uvjet = False
treci_uvjet = True

predavac = 'Filip'

# Jednostavni primjer:
if prvi_uvjet:
    # izvrsi instrukcije SAMO AKO je prvi_uvjet točan ili ima vrijednost TRUE
    print('Usli smo u if dio') 
else:
    # ako prethodni uvjet nije ispunjen, njegova vrijednost je FALSE
    # tada izvrši naredbe iz ovog bloka
    print('Usli smo u else dio')

# Niz uvjeta prije ELSE.
# Ako poslije IF uvjeta trebamo napraviti još jednu provjeru tada pišemo ELSE IF uvjet, 
# a u Pythonu je to skraćeno i piše se ELIF poslije koje dolazi novi uvjet
if prvi_uvjet:
    # izvrsi instrukcije SAMO AKO je prvi_uvjet točan ili ima vrijednost TRUE
    pass
elif drugi_uvjet:
    # Ako prvi uvjet NIJE zadovoljen, znači da je prvi_uvjet NEtočan, ima vrijednost False
    # Tada je izvršavanje programa došlo do ove linije pa OPET slijedi provjera
    # AKO je drugi_uvjet točan ili ima vrijednost True izvrši instrukcije u ovom bloku
    pass
elif treci_uvjet:
    # isto kao i za drugi_uvjet
    pass
else:
    # Ako niti jedan od uvjeta NIJE ispunjen, svi su FALSE
    # Tada bez obzira na UVJETE i VRIJEDNOSTI IZVRŠI aktivnosti iz ovog bloka
    pass


# ELSE najčešće koristimo kao slučaj koji pokriva sve one uvjete koje nismo naveli ili nema smisla navoditi

# ZADATAK !!
# Kreirajte listu brojeva od 1 do 30
brojevi = []
for broj in range(1, 31):
    brojevi.append(broj)

# Provjera je li broj djeljiv s nekim drugim (pomoću modulo % operatora)
# Ispišite sve brojeve koji su djeljivi s 3, 6 i 9

# for broj in brojevi:
#     if broj % 3 == 0:
#         print(f'Broj {broj} je djeljiv s 3!')
#     elif broj % 6 == 0:
#         print(f'Broj{broj} je djeljiv s 6!')
#     elif broj % 9 == 0:
#         print(f'Broj {broj} je djeljiv s 9!')
#     else:
#         print(f'Broj {broj} nije djeljiv s 3, 6, ili 9!')

"""
Broj 1 nije djeljiv s 3, 6, ili 9!
Broj 2 nije djeljiv s 3, 6, ili 9!
Broj 3 je djeljiv s 3!
Broj 4 nije djeljiv s 3, 6, ili 9!
Broj 5 nije djeljiv s 3, 6, ili 9!
Broj 6 je djeljiv s 3!
Broj 7 nije djeljiv s 3, 6, ili 9!
Broj 8 nije djeljiv s 3, 6, ili 9!
Broj 9 je djeljiv s 3!
Broj 10 nije djeljiv s 3, 6, ili 9!
Broj 11 nije djeljiv s 3, 6, ili 9!
Broj 12 je djeljiv s 3!
"""

# Pitanje: Zašto je ovo krivo? Kako to riješiti? 
# Odgovor: Ovo je primjer kada nam IF iz kojeg slijedi ELIF ne pomaže, nego moramo koristiti IF pa iza njega ponovno IF.
            # Razlika je u tome što IF + ELIF + ELIF ... predstavljaju jednu povezanu cjelinu !!
            # IF + IF + IF ... predstavlja odvojene dijelove koda koji rade svaki za sebe !! 
            # Ako nam je jedan uvjet ispunjen, svejedno će se provjeravati sljedeći IF.

for broj in brojevi:
    if broj % 9 == 0:
        print(f'Broj {broj} je djeljiv s 9')
    if broj % 6 == 0:
        print(f'Broj {broj} je djeljiv sa 6')
    if broj % 3 == 0:
        print(f'Broj {broj} je djeljiv s 3')
    else:
        print(f'Broj {broj} NIJE djeljiv s 3, 6 ili 9')

# zadnji IF i ELSE blok su POVEZANI!!


