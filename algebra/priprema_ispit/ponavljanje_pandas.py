import pandas as pd

podaci = {
    'Ime': ['Ana', 'Ivan', 'Marko', 'Ema', 'Petra', 'Luka', 'Mia', 'Matija', 'Ana', 'Filip', 'Lucija', 'Ante', 'Tea', 'Roko', 'Iva', 'Borna', 'Lea', 'Nikola', 'Sara', 'Ivan'],
    'Prezime': ['Kovačević', 'Horvat', 'Marić', 'Šimunović', 'Babić', 'Vuković', 'Pavić', 'Matić', 'Jurić', 'Perić', 'Knežević', 'Blažević', 'Kovačić', 'Tomić', 'Šimić', 'Kovač', 'Rukavina', 'Petrović', 'Kolar', 'Kovačević'],
    'Godina_studija': [2, 3, 1, 3, 2, 1, 2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 1],
    'Ocjena': [4.2, 3.8, 4.9, 4.1, 3.5, 4.7, 3.9, 4.5, 4.0, 4.6, 4.2, 3.7, 4.8, 4.0, 3.6, 4.5, 3.8, 4.3, 4.2, 4.6],
    'Fakultet': ['FER', 'PMF', 'EFZG', 'FER', 'PMF', 'EFZG', 'FER', 'EFZG', 'PMF', 'FER', 'EFZG', 'PMF', 'FER', 'EFZG', 'PMF', 'EFZG', 'FER', 'PMF', 'EFZG', 'PMF']
}

df = pd.DataFrame(podaci)

# Filtriraj prema godini studija
studenti_treca_godina = df[df['Godina_studija'] == 3]
print(studenti_treca_godina)

# Prosječna ocjena po fakultetu
prosjek_po_fakultetu = df.groupby('Fakultet')['Ocjena'].mean()
print(prosjek_po_fakultetu)

# Sortiraj studente po prosječnoj ocjeni
sortirani_studenti = df.sort_values(by='Ocjena', ascending = False)
print(sortirani_studenti)

# Dodaj novi stupac status - ako je ocjena veća od 4.0 ispit je položen, inače nije položen
df['Status'] = df['Ocjena'].apply(lambda ocjena: 'Ispit položen' if ocjena > 4.0 else 'Ispit nije položen')
print(df)

# Filtriraj sve FERovce s ocjenom većom od 4.0
fer_polozili = df[(df['Fakultet'] == 'FER') & (df['Ocjena'] > 4.0)]
print(fer_polozili)

# Izračunaj broj studenata po godinama studija
broj_studenata_po_godinama = df['Godina_studija'].value_counts()
print(broj_studenata_po_godinama)

# SPremanje u CSV file
df.to_csv('rezultati.csv', index = False)

