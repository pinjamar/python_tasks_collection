racun_broj = 'R-1-2023-06'
racun_datum_izdavanja = '21.06.2023'
racun_stavke = {'Laptop': 1500.00,
                'Torba za laptop': 300.00,
                'Monitor': 550.50,
                'Python za pocetnike': 23.77}
popust = 10

racun_ukupan_iznos = 0
for stavka in racun_stavke.values():
    racun_ukupan_iznos += stavka

racun_ukupan_iznos = racun_ukupan_iznos - racun_ukupan_iznos * popust

# Izračunajmo iznos PDV-a
racun_iznos_pdv = racun_ukupan_iznos * 0.25

# Ispis računa
print('\n\n')
print('*' * 50)
print(f'\n\tRACUN:\t\t{racun_broj}')
print(f'\tDATUM::\t\t{racun_datum_izdavanja}\n')
print('-' * 50)
print('\n\tProizvod\t\tCijena')
for proizvod, cijena in racun_stavke.items():
    print(f'\t{proizvod}\t{cijena} kn')

print('\n')
print('-' * 50)
print(f'\n\tIZNOS PDV-a:\t{racun_iznos_pdv}')
print(f'\tUKUPAN IZNOS:\t{racun_ukupan_iznos}\n')
print(f'Popust: {popust}')
print('*' * 50)
print('\n\n')

racuni = {
    'R-1-2023-06': {
        'stavke': ['Laptop', 'Torba za laptop'],
        'cijene': [1500, 300],
        'pdv': 60,
        'ukupan_iznos': 3000,
        'popust': 10
    },
    'R-2-2023-06': {}
}