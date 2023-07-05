### 1. KORAK ###
# Uključiti sqlite3 modul u našu aplikaciju
import sqlite3

### 2. KORAK ###
# Kreirajmo varijablu u koju ćemo pohraniti naš QUERY ili UPIT
# Taj QUERY će se kasnije izvršavati pomoću execute() metode !
# Dodati ćemo podatke u Employees tablicu

insert_into_table_query = '''INSERT INTO Employees (name, email)
                             VALUES (?, ?)'''

database_name = 'TvrtkaDb.db'

### 3. KORAK ###
# Kreirajmo list djelatnika
lista_djelatnika = [
    ('Petar Peric', 'pperic@email.com'),
    ('Ana Anic', 'aanic@email.com'),
    ('Kresimir Horvat', 'khorvat@email.com')
]

# Za otvaranje konekcije, pisanje ili čitanje iz baze koristit ćemo try - except - finally blok naredbi
try:
    # Kreirat ćemo konekciju prema SQLite bazi, to je u stvari datoteka čije ime proslijedimo u connect() metodi
    # Ako datoteka ne postoji, Python će je kreirati
    sqlite_connection = sqlite3.connect(database_name)

    ### 4. KORAK ###
    # Kreirat ćemo CURSOR objekt koji je zadužen za sve aktivnosti prema SQLite bazi

    cursor = sqlite_connection.cursor()
    print("Baza je USPJEŠNO kreirana i aplikacija spojena na SQLite")

    # Pomoću execute() metode na CURSOR-u pokrenimo prethodno pripremljeni query
    for djelatnik in lista_djelatnika:
        cursor.execute(insert_into_table_query, djelatnik)

    # Pomoću commit() metode na CURSOR objektu pokrenimo prethodno pripremljeni query
    sqlite_connection.commit()

    # Prikažimo rezultat koji smo dobili
    print("Podaci su uspješno importani!")

    ### 5. KORAK ###
    # Moramo otpustiti resurse koje smo uzeli kreirajući CURSOR objekt
    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspješno otpušteni")

# AKO JE DOŠLO DO GREŠKE, obrađujemo je u except bloku
except sqlite3.Error as error:
    print("ERROR - Dogodila se greška: ", error)

### 6. KORAK ###
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija je uspješno zatvorena!")

