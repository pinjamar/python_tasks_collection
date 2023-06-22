# ZADATAK: Name i email manager. Napišite Python program koji sprema imena i email adrese u rječnik.
# Ime je ključ (ime i prezime), a email je vrijednost! 

# Program mora imati glavni izbornik koji omogućuje korisniku da:
    # 1. Pogleda sva imena i mailove u rječniku
    # 2. Pronađe specifični kontakt (unese ime i prezime, a dobije email)
    # 3. Doda kontakt
    # 4. Uredi kontakt
    # 5. Izbriše kontakt
    # 6. Izađe iz programa

import os

moj_adresar = {
    "Filip Skendrovic": "filip.skendrovic@predavaci.algebra.hr",
    "Pero Peric": "pero.peric@gmail.com"
}

def main_menu():
    print("Name and Email Manager")
    print("------------------------")
    print("1. Ispiši sve kontakte")
    print("2. Pronađi specifični kontakt")
    print("3. Dodaj novi kontakt")
    print("4. Uredi kontakt")
    print("5. Izbriši kontakt")
    print("6. Izađi iz programa")

def view_all_contacts(contacts):
    # Želimo ispis oblike ime (email)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nKontakti iz adresara:")
    print("-----------------------")
    for name, email in contacts.items():
        print(name, f"({email})")
    
    input('Press ENTER to continue...')
    print()

def view_contact(contacts):
    os.system('cls' if os.name == 'nt' else 'clear')
    print()

    ime = input('Unesite ime kontakta čiji email želite pronaći')
    email = ""

    for key in contacts.keys():
        if ime.lower() == key.lower():
            email = contacts[key]
    
    print()
    if len(email) != 0:
        print(f"{ime} ({email})")
    else:
        print('Specificarno ime ne postoji u rječniku!')

    input('Press ENTER to continue...')
    print()

    # pitati korisnika da unese ime čije email želi pronaći ! Potrebno je isprintati ime i pripadajući email

def add_contact(contacts):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nUnesi ime i email adresu kontakta koji želite dodati")
    ime = input("Ime:\t")
    email = input("Email:\t")

    kontakt_postoji = False

    for key in contacts.keys():
        if key.lower() == ime.lower():
            print("Specificirani korisnik već postoji!")
            kontakt_postoji = True
            break
    
    contacts[ime] = email
    print("\nKontakt je uspješno dodan!")

    input('Press ENTER to continue...')
    print()
    # pitati korisnika da unese ime i prezime, te email i pohraniti ga u rječnik

def edit_contact(contacts):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Ovdje će marljivi polaznici dodati logiku za edit contact')
    input('Press ENTER to continue...')
    print()

    # pitati korisnika da unese ime kontakta koji želi promijeniti, uklonite to ime iz rječnika, zatražite
    # korisnika da unese novo ime i email i tako pohranite

def delete_contact(contacts):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Ovdje će marljivi polaznici dodati logiku za delete contact')
    input('Press ENTER to continue...')
    print()
    # pitati korisnika da unese ime kontakta koji želi ukloniti i ukloniti ga, naravno ako se unese nepostojeći
    # kontakt ispisati poruku da ime ne postoji


izbor_korisnika = -1
while izbor_korisnika != 6:
    main_menu()

    izbor_korisnika = input("Izaberi 1-6:\t")
    while not (izbor_korisnika.isdigit() == True and int(izbor_korisnika) >= 1 and int(izbor_korisnika) <= 6):
        print("Unesite validan broj između 1 i 6.")
        izbor_korisnika = input("Izaberi 1-6:\t")

    izbor_korisnika = int(izbor_korisnika)

    if izbor_korisnika == 1:
        view_all_contacts(moj_adresar)
    elif izbor_korisnika == 2:
        view_contact(moj_adresar)
    elif izbor_korisnika == 3:
        add_contact(moj_adresar)
    elif izbor_korisnika == 4:
        edit_contact(moj_adresar)
    elif izbor_korisnika == 5:
        delete_contact(moj_adresar)