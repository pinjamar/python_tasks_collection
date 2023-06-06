### KORISNIČKI DEFINIRANE FUNKCIJE ###

# kljucna rijec DEF:
def pozdrav(ime):
    """
    Funkcije koja na konzolu ispisuje pozdravnu poruku osobi 
    cije ime je proslijeđeno u funkciju kao parametar
    """
    print(f'Dobar dan, {ime}. Kako ste danas?')

# Poziv funkcije:
# pozdrav('Stjepan')
# pozdrav('Krešimir')

# Pristup dokumentaciji funkcije - docstring
# print(pozdrav.__doc__)
# Ovaj dio koda ispisuje tekst koji je naveden unutar docstring bloka prilikom deklaracije funkcije!

######################################################################################################

# kljucna rijec DEF:
def pozdrav_naprednije(ime, odg_pozdrav):
    """
    Funkcije koja na konzolu ispisuje pozdravnu poruku osobi 
    cije ime je proslijeđeno u funkciju kao parametar
    """
    print(f'{odg_pozdrav}, {ime}. Kako ste danas?')

# Poziv funkcije:
# pozdrav_naprednije('Stjepan', 'Dobar dan')
# pozdrav_naprednije('Krešimir', 'Dobro jutro')

######################################################################################################

# Dodat ćemo modul za rad s vremenskim varijablama
import datetime

# print(datetime.datetime.now())
def pozdrav(ime):
    """
    Funkcija koja ovisno o dobu dana vrati pozdravnu poruku za osobu čije ime je argument funkcije.
    Ako je vrijeme poziva funkcije prijepodne poruka glasi 'Dobro jutro, IME. Danas je novi dan.
    Ako je vrijeme poziva funkcije poslijepodne poruka glasi 'Dobar dan, IME. Danas vam super ide, samo nastavite tako!
    Ako je vrijeme poziva funkcije navečer poruka glasi 'Dobra večer, IME. Danasnji dan je bio uspješan!
    """
    # trenutni_sati = datetime.datetime.now().hour
    # if trenutni_sati...
        
    # trenutno_vrijeme = datetime.datetime.now()
    # if trenutno_vrijeme.hour...

    if datetime.datetime.now().hour < 12:
        return f'\nDobro jutro, {ime}. Danas je novi dan.\n'
    elif datetime.datetime.now().hour > 12 and datetime.datetime.now().hour < 19:
        return f'\nDobar dan, {ime}. Danas vam super ide, samo nastavite tako!\n'
    else:
        return f'\nDobra večer, {ime}. Danasnji dan je bio uspješan.\n'
    
# Poziv funkcije:
pozdravna_poruka = pozdrav('Petar')
# pozdravna_poruka = pozdrav('Petar')

# print(pozdravna_poruka)

now = datetime.datetime.now()
print(now)
current_time = now.strftime("%H")
print(current_time)

