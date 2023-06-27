### PISANJE - WRITE - 'W' ###

# counter = 1
# while True:
#     ime = input('Upisite ime kontakta: ')
#     prezime = input('Upisite prezime kontakta: ')
#     mobitel = input('Upisite broj mobilnog telefona: ')

#     # 1. Otvorite konekciju prema datoteci
#     file_writer = open('adresar.txt', 'w')
#     # 2. Zapišite sadržaj u datoteku Rb;Ime;Prezime;Mobitel
#     file_writer.write(f'{counter};{ime};{prezime};{mobitel}')
#     counter += 1
#     # 3. Zatvorite datoteku
#     file_writer.close()

#     if input('Zelite li unijeti novi kontakt? (da/ne) ') != 'da':
#         break

# Pokušaj 2 - Adresar
# counter = 1

# # 1. Otvorite konekciju prema datoteci
# file_writer = open('adresar.txt', 'w')

# while True:
#     ime = input('Upisite ime kontakta: ')
#     prezime = input('Upisite prezime kontakta: ')
#     mobitel = input('Upisite broj mobilnog telefona: ')

#     # 2. Zapišite sadržaj u datoteku Rb;Ime;Prezime;Mobitel
#     file_writer.write(f'{counter};{ime};{prezime};{mobitel}')
#     counter += 1

#     if input('Zelite li unijeti novi kontakt? (da/ne) ') != 'da':
#         break

# # 3. Zatvorite datoteku
# file_writer.close()

# Pokušaj 3  - Adresar
# counter = 1
# while True:
#     ime = input('Upisite ime kontakta: ')
#     prezime = input('Upisite prezime kontakta: ')
#     mobitel = input('Upisite broj mobilnog telefona: ')

#     # 1. Otvorite konekciju prema datoteci
#     file_writer = open('adresar.txt', 'a')
#     # 2. Zapišite sadržaj u datoteku Rb;Ime;Prezime;Mobitel
#     file_writer.write(f'{counter};{ime};{prezime};{mobitel}\n')
#     counter += 1
#     # 3. Zatvorite datoteku
#     file_writer.close()

#     if input('Zelite li unijeti novi kontakt? (da/ne) ') != 'da':
#         break

### Adresar - Pokušaj 4 ###
# counter = 1
# while True:
#     ime = input('Upisite ime kontakta: ')
#     prezime = input('Upisite prezime kontakta: ')
#     mobitel = input('Upisite broj mobilnog telefona: ')

#     try:
#         file_writer = open('adresar.txt', 'a')
#         file_writer.write(f'{counter};{ime};{prezime};{mobitel}\n')
#         counter += 1
    
#     except Exception as e:
#         print(f'Dogodila se greška {e}')

#     finally:
#         # Bez obzira je li se dogodila greška ili nije UVIJEK zatvaramo komunikaciju prema datoteci
#         file_writer.close()

#     if input('Zelite li unijeti novi kontakt? (da/ne) ') != 'da':
#         break

# Python ima jednostavniji način otvaranja komunikacije prema datotekama
# ključna riječ with  koja u sebi sadrži zatvaranje konekcije, znači ne moramo koristiti finally!
counter = 1
while True:
    ime = input('Upisite ime kontakta: ')
    prezime = input('Upisite prezime kontakta: ')
    mobitel = input('Upisite broj mobilnog telefona: ')

    try:
        with open('adresar.txt', 'a') as file_writer:
            file_writer.write(f'{counter};{ime};{prezime};{mobitel}\n')
            counter += 1
    
    except Exception as e:
        print(f'Dogodila se greška {e}')

    if input('Zelite li unijeti novi kontakt? (da/ne) ') != 'da':
        break
