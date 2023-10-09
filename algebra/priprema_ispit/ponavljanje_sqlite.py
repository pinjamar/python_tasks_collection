import sqlite3

conn = sqlite3.connect('baza_podataka.db')

cursor = conn.cursor()

sql_create_table_query = '''
CREATE TABLE IF NOT EXISTS osobe (
    id INTEGER PRIMARY KEY,
    ime TEXT,
    prezime TEXT
)'''

cursor.execute(sql_create_table_query)

conn.commit()
conn.close()

def unos_osobe():
    conn = sqlite3.connect('baza_podataka.db')
    cursor = conn.cursor()

    ime = input("Unesi ime osobe:\t")
    prezime = input("Unesi prezime osobe:\t")

    sql_insert_into = '''
    INSERT INTO osobe (ime, prezime) VALUES (?, ?)'''

    cursor.execute(sql_insert_into, (ime, prezime))

    conn.commit()
    conn.close()

def ispisi_osobe():
    conn = sqlite3.connect('baza_podataka.db')
    cursor = conn.cursor()

    sql_select_all = '''
    SELECT * FROM osobe'''

    cursor.execute(sql_select_all)
    osobe = cursor.fetchall()

    for osoba in osobe:
        print(f"ID: {osoba[0]}, Ime: {osoba[1]}, Prezime: {osoba[2]}")
    conn.close()

while True:
    print("1. Unesi novu osobu")
    print("2. Ispiši sve osobe")
    print("3. Izađi iz programa")

    izbor = input("Odaberite opciju: ")

    if izbor == '1':
        unos_osobe()
    elif izbor == '2':
        ispisi_osobe()
    elif izbor == '3':
        break
    else:
        print("Odabrali ste nepostojeću mogućnost, pokušajte ponovno.")
