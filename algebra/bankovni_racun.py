# SIMULACIJA BANKOVNOG RAČUNA

# Zadatak je započet, a polaznici nastavljaju dalje po predlošku

import datetime
import os

# GLOBALNE VARIJABLE
company_name = ''
company_street_and_number = ''
company_postal_code = ''
company_city = ''
company_tax_id = ''
company_manager = ''
currency = 'HRK'

# Treba nam neki dictionary u koji ćemo pohranjivati informacije o transakcijama
transaction_id = 0
transactions = {}

# Format računa je oblika BA-GODINA-MJESEC-REDNI_BROJ
# BA - Business Account
# Redni broj 00001 - 5 znamenki

account_number = ''
account_balance = 0.00

def generate_account_number():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    if month < 10:
        month = '0' + str(month) # ako je mjesec svibanje vratit će '05'
    else:
        month = str(month)

    # ako želimo da nam se broj na kraju automatski povećava koristit ćemo if - else -> ako je '' onda je broj 00001
    # a ako nije prazan string možemo koristiti split('-') 
    # BA-2023-06-00001 -> nakon split('-') dobit ćemo listu s elementima BA 2023 06 i neki broj (00045 -> int(00045) = 45)
    # if elif blok za određivanje vodećih 0 u rednom broju računa !

    account_number = 'BA-' + str(year) + '-' + month + '-00001'
    return account_number


def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = -1
    print('*' * 65)
    print('PyBank Algebra\n'.center(65), '\n')
    print('GLAVNI IZBORNIK\n'.center(65))

    if company_name == '':
        print('1. Kreiranje računa')
    else:
        print('1. Ažuriranje računa')
    
    print('2. Prikaz stanja računa')
    print('3. Prikaz prometa po računu')
    print('4. Polog novca na račun')
    print('5. Podizanje novca s računa')
    print('0. Izlaz')

    print('_' * 65)

    if company_name == '':
        while choice != 1 and choice != 0:
            print('Još niste otvorili račun. Molim prvo kreirajte račun! Hvala!')
            print('-' * 65)
            choice = int(input('Molimo unesite broj između 0 ili 1!'))
            print()
    else:
        while not (int(choice) >= 0 and int(choice) <= 5):
            print("Upisite broj ispred opcije koju zelite odabrati!")
            choice = int(input('Molimo unesite broj između 0 i 5!'))

    return choice

def create_transaction():
    pass

def kreiranje_racuna_menu():
    print('*' * 65)
    print('PyBank Algebra\n\n'.center(65))
    print('Kreiranje računa\n'.center(65))
    

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_account():
    clear_terminal()
    kreiranje_racuna_menu()
    print('Podaci o vlasniku računa\n'.center(65))

    global company_name
    global company_street_and_number
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global account_balance

    company_name = input('Naziv tvrtke:\t\t\t\t')
    company_street_and_number = input('Ulica i broj sjedišta tvrtke:\t\t')
    company_postal_code = input('Postanski broj sjedista tvrtke:\t\t')
    company_city = input('Grad u kojem je sjedište tvrtke:\t')
    company_tax_id = input('OIB Tvrtke:\t\t\t\t')
    while len(company_tax_id) != 11 and company_tax_id.isdigit():
        print('OIB mora imati točno 11 znamenki i mora sadržavati brojeve. Molim pokušajte ponovno!')
        company_tax_id = input('OIB Tvrtke:\t\t\t\t')
    company_manager = input(' Ime i prezime odgovorne osobe tvrtke:\t')
    print()
    currency = input('Upisite naziv valute računa (EUR ili HRK):\t')
    if currency.upper() == 'HRK':
        currency = 'hr'
    else:
        currency = '€'

    input('\nSPREMI? (Pritisnite bilo koju tipku)')

    clear_terminal()
    kreiranje_racuna_menu()
    print(f'Podaci o vlasniku računa tvrtke {company_name} su uspješno spremljeni.')
    input('Za nastavak pritisnite bilo koju tipku\t')

    clear_terminal()
    kreiranje_racuna_menu()
    print('Stanje računa\n'.center(65), '\n')

    print(f'Broj računa {generate_account_number()}')
    print(f'Trenutno stanje računa:\t{account_balance}{currency}\n')
    print('Molimo vas upišite iznos koji želite položiti na račun.')
    print('Molimo vas koristite decimalnu točku, a ne zarez')
    amount = input('\t')
    if amount != '':
        amount = float(amount)

        transaction = []
        account_balance += amount

        # transakcija - dodajemo datum, vrijeme, iznos, stanje, broj racuna, opis, ime managera
        transaction.append(datetime.datetime.date)
        transaction.append(datetime.datetime.time)
        transaction.append(amount)
        transaction.append(account_balance)
        transaction.append(account_number)
        transaction.append('Polog kod otvaranja računa')
        transaction.append(company_manager)
        transactions[transaction_id + 1] = transaction
    else:
        amount = 0.00
  
def display_account_balance():
    clear_terminal()
    print('*' * 65)
    print('PyBank Algebra\n\n'.center(65))
    print('Prikaz stanja računa\n'.center(65))

    print(f'Broj racuna\t{account_number}')
    print(f'Datumi vrijeme:\t{datetime.datetime.now()}\n')

    print(f'Trenutno stanje racuna:\t{account_balance}{currency}\n\n')

    print('-') * 65
    input('Za povratak u glavni izbornik pritisnite bilo koju tipku\t')


def display_historical_transactions():
    pass

choice = main_menu()
while choice != 0:
    if choice == 1 and company_name == '':
        open_account()
    if choice == 1 and company_name != '':
        # update_account()
        pass
    if choice == 2:
        display_account_balance()
    if choice == 3:
        display_historical_transactions()
    if choice == 4:
        # create_deposit_transaction()
        pass
    if choice == 5:
        # create_withdrawal_transaction()
        pass

    choice = main_menu()

