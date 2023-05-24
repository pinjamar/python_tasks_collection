# ZADATAK:  generickom tekstu Lorem Ipsum.... pronađite koliko puta se pojavljuje neka zadana rijec

# SAVJET: Tekst koji se prostire u vise redaka i koji zelimo dodati u jednu varijablu
# trebamo staviti izmedu tri navodnika na pocetku i na kraju - docstring

tekst = ('Sed ut perspiciatis unde omnis iste natus error sit voluptatem '
         'accusantium doloremque laudantium, totam rem aperiam, eaque ipsa '
         'quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. '
         'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, '
         'sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. '
         'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, '
         'sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. '
         'Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, '
         'nisi ut aliquid ex ea commodi consequatur. Quis autem vel eum iure reprehenderit '
         'qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem '
         'eum fugiat quo voluptas nulla pariatur.')


print('\n', tekst, '\n')

# Naredba tekst.lower() sva velika slova prebaci u mala slova, upper() radi obrnuto
tekst_lower = tekst.lower()
print(tekst_lower)

# naredba tekst.split() prodje kroz cijeli tekst i kad naide na znak pohrani rijec u listu
lista_rijeci = tekst_lower.split(" ")
print(lista_rijeci)

for rijec in lista_rijeci:
    # zelimo maknuti tocku ako ona postoji u rijeci
    if "." in rijec:
        # treba tocno odrediti koji element liste cemo azurirati
        # dodjeljivanje vrijoednosti nekom elmentu liste _> lista[indeks] = nova_vrijednost
        # naredbom replace("sto", "cime") zamjenjujemo sto s cime ! _> replace(".","")
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace(".", "")
    elif "," in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace(",", "")

# treba nam varijabla u koju cemo pohraniti koliko puta se pojavljuje trazena rijec
brojac = 0

trazena_rijec = input(
    "Upisite rijec za koju zelite provjeriti broj ponavljanja:")

# savjet: kada usporedjujemo tekst koji je unio korisnik s ekstom koji imamo u varijabli uvijek je praksa prebaciti cijeli tekst i korisnikov tekt u velika / mala slova
trazena_rijec_lower = trazena_rijec.lower()

for rijec in lista_rijeci:
    if rijec == trazena_rijec_lower:
        brojac += 1


# ispisimo koliko puta se pojavljuje trazena rijec
print(f'Rijec {trazena_rijec_lower} se u tekstu pojavljuje {brojac} puta')

# ako prilikom rastavljanja teksta (split) stavimo razdvajanje po razmaku onda neke rijeci mogu upasti zajedno s . ili , pa ne broji kako treba (bug)
# rjesenje je dodatno prociscavanje teksta
