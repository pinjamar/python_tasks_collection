### OSNOVNI KORACI ###

### Pisanje - Write - 'W' ###
# 1. Otvorite datoteku za pisanje.
    # Kreirajte varijable u koju ćete pohraniti konekciju prema datoteci.
    # Naziv varijable je proizvoljan pa neka bude jasno što radi 
    # Pomoću metode open() definirajte naziv varijable kao prvi argument
    # Ako datoteka ne postoji, Python će je kreirati.
    # Kao drugi argument definirajte aktivnost koju želite napraviti 
    # U našem primjeru će to biti 'w' - write za pisanje

file_writer = open("ime.txt", 'w')

# 2. Zapiši sadržaj
# Definiramo sadržaj koji ćemo zapisati u datoteku

ime = input('Unesite vaše ime i prezime: ')

# Zapišite sadržaj u datoteku
file_writer.write(ime)

# 3. Korak - zatvorite datoteku
file_writer.close()

### ČITANJE - READ - 'R' ###
    # Sve je isto kao i kod pisanja, jedino sada u metodi open() kao drugi argument navodimo 'r'
# 1. Otvorite datoteku za čitanje

file_reader = open('ime.txt', 'r')

# 2. Kreirajte varijablu u koju želite pohraniti sadržaj datoteke
file_data = file_reader.read()

# 3. Zatvorite datoteku
file_reader.close()

print(f'Sadrzaj datoteke je\n{file_data}')
