### 1. KORAK ###
# Uključiti sqlite3 modul u našu aplikaciju
import sqlite3

### 2. KORAK ###
# Kreirajmo varijablu u koju ćemo pohraniti naš QUERY ili UPIT
# Taj QUERY će se kasnije izvršavati pomoću execute() metode !
# Kreirat ćemo tablicu Employees

create_table_query = '''CREATE TABLE IF NOT EXISTS Employees (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE);'''

database_name = 'TvrtkaDb.db'

### 3. KORAK ###
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
    cursor.execute(create_table_query)

    # Pomoću commit() metode na CURSOR objektu pokrenimo prethodno pripremljeni query
    sqlite_connection.commit()

    # Prikažimo rezultat koji smo dobili
    print("Nova tablica Employees je kreirana!")

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

