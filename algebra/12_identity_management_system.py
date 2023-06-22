# zadatak: kreirajte predefinirani administrator sustava koji moze dodati novog korisnika u sustav
# azurirati postojece korisnike i brisati postojece korisnike

# svaki nas korisnik ima 4 podatka, ime, prezime, username, password
# password mora sadrzavati najmanje 10 znakova
# korisnicko ime (username) mora biti jedinstveno

# nakon sto se korisnik uspjesno prijavi, na ekranu se ispisuje poruka "Dobro dosli, {ime} i {prezime}"

# upute: potrebno je kreirati jedan rjecnik (dict) u kojem je kljuc username, a vrijednost je lista koja sadrzi ime, prezime, password
# pocetni rjecnik vec ima 1 element, a to je administrator sustava

# potrebno je kreirati funkcije za:
# 1 prikaz izbornika
# 2 provjeru prijave
# 3 dodavanje novih korisnika
# 4 azuriranje novih korisnika
# 5 ako ulogirani korisnik ima isti username kao administrator onda on u prikazu izbornika dodatno vidi mogucnost brisanja korisnika
# znaci, samo admin vidi u izborniku mogucnost brisanja i moze tu mogucnost koristiti

import os

sustav = {
    "admin": ["admin1", "admin2", "admin3"],
    "pero123": ["pero", "peric", "123456"]
}


def main_menu(user_logged_in):
    print("------------------------")
    print("1. Dodavanje novih kontakata")
    print("2. Azuriranje kontakt")
    print("3. Ispis kontakata")
    print("4. Izbrisi kontakt")
    if user_logged_in == "admin":
        print("5. Izbriši kontakt")
    print("0. Izađi iz programa")


def login():
    username = input("Dobro dosli, molim vas unesite vase ime: ").lower()
    password = input("Unesite vasu sifru: ").lower()
    for key, value in sustav.items():
        if key == username and password == value[2]:
            print(f"Dobrodosli {value[0]} {value[1]}")
            # main_menu(username)
        else:
            print("Korisnicko ime ne postoji")
    return username


def dodavanje_novog_korisnika():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nUnesi korisnicko ime, ime, prezime te vasu sifru: ")
    username = input("Unesite korisnicko ime:\t").lower()
    for key in sustav.keys():
        while key.lower() == username.lower():
            print("Specificirani korisnik već postoji!")
            username = input("Unesite korisnicko ime:\t").lower()
    ime = input("Unesite vase ime:\t").lower()
    prezime = input("Unesite vase prezime:\t").lower()
    password = input("Unesite vasu sifru:\t").lower()
    while len(password) < 10:
        print("Prekratka sifra! Pokusajte ponovno.")
        password = input("Unesite zeljenu sifru: ").lower()
    sustav[username] = [ime, prezime, password]


def azuriranje_korisnika():
    os.system('cls' if os.name == 'nt' else 'clear')
    odabir = input(
        "Odaberite cije podatke zelite promijeniti\n1)Ime 2)Prezime 3)Sifru")
    sustav[odabir] = input(
        "Odaberite cije podatke zelite promijeniti: ").lower()
    promjena_ime = input("Unesite novo zeljeno ime: ").lower()
    promjena_prezime = input("Unesite novo prezime: ").lower()
    promjena_password = input("Unesite novu zeljenu sifru: ").lower()
    while len(promjena_password) < 10:
        print("Unijeli ste prekratku sifru! Pokusajte ponovno.")
        promjena_password = input("Unesite novu zeljenu sifru: ").lower().lower
    sustav[odabir] = [promjena_ime, promjena_prezime, promjena_password]


def brisanje_korisnika():
    odabir = input("Odaberite kojeg korisnika zelite obrisati").lower()
    if odabir == "admin":
        print("Ne mozete obrisati administratora! Pokusajte ponovno:")
        odabir = input("Odaberite kojeg korisnika zelite obrisati").lower()
    sustav.pop(odabir)


izbor_korisnika = -1
user_logged_in = ""
while izbor_korisnika != 0:
    if user_logged_in == "":
        user_logged_in = login()
        main_menu(user_logged_in)
    else:
        main_menu(user_logged_in)

    izbor_korisnika = input("Izaberi 0-4:\t")
    while not (izbor_korisnika.isdigit() == True and int(izbor_korisnika) >= 0 and int(izbor_korisnika) <= 4):
        print("Unesite validan broj između 0 i 4.")
        izbor_korisnika = input("Izaberi 0-4:\t")

    izbor_korisnika = int(izbor_korisnika)

    if izbor_korisnika == 1:
        dodavanje_novog_korisnika()
    elif izbor_korisnika == 2:
        azuriranje_korisnika()
    elif izbor_korisnika == 3:
        print(sustav)
    elif izbor_korisnika == 4:
        brisanje_korisnika()
    elif izbor_korisnika == 0:
        print("Izlazak iz programa")
        break

print(sustav)
