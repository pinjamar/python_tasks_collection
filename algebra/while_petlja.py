### IF petlja je imala uvjet koji ako je ispunjen izvršava se blok programskom koda unutar te petlje SAMO JEDNOM !
# Nakon što je uvjet ispunjen, izvršava se kod izvan IF petlje

# WHILE je slična, ima uvjet koji ako je ispunjen, osigurava pokretanje bloka programskog koda unutar WHILE petlje
# Nakon završetka tog bloka programskog kod, WHILE će ponoviti provjeru uvjeta !! 

brojevi = []
for broj in range(1, 21):
    brojevi.append(broj)

# Ispis brojeva pomoću FOR petlje:
# for broj in brojevi:
#     print(broj, end=' ')

# Ispis elemenata pomoću WHILE petlje:
# Treba nam varijabla koja će služiti za provjeru koliko puta smo ponovili blok while petlje
brojac = 0

# SVE DOK (while) je brojac manji od broja elemenata liste IZVRŠAVAJ:
while brojac < len(brojevi):
    print(brojevi[brojac], end = ' ')
    # Povecaj brojac za 1 i napravi provjeru:
    # brojac += 1