class Racun:
    '''
    Klasa za upravljanje računima
    '''

    def __init__(self,
                 racun_broj,
                 racun_datum_izdavanja,
                 racun_stavke,
                 iznos_pdv):
        self.racun_broj = racun_broj
        self.racun_datum_izdavanja = racun_datum_izdavanja
        self.racun_stavke = racun_stavke
        self.iznos_pdv = iznos_pdv
        self.racun_ukupan_iznos = 0

        self.izracunaj_ukupan_iznos()

    def izracunaj_ukupan_iznos(self):
        for cijena in self.racun_stavke.values():
            self.racun_ukupan_iznos += cijena

    def izracunaj_pdv(self, iznos):
        return iznos * self.iznos_pdv

    def ispisi_racun(self):
        print('\n\n')
        print('*' * 50)
        print(f'\n\tRACUN:\t\t{self.racun_broj}')
        print(f'\tDATUM::\t\t{self.racun_datum_izdavanja}\n')
        print('-' * 50)
        print('\n\tProizvod\t\tCijena')
        for proizvod, cijena in self.racun_stavke.items():
            print(f'\t{proizvod}\t{cijena} kn')

        print('\n')
        print('-' * 50)
        print(
            f'\n\tIZNOS PDV-a:\t{self.izracunaj_pdv(self.racun_ukupan_iznos)}')
        print(
            f'\tUKUPAN IZNOS:\t{self.racun_ukupan_iznos + self.izracunaj_pdv(self.racun_ukupan_iznos)}\n')
        print('*' * 50)
        print('\n\n')


def kreiraj_racun(brojac_racuna, pdv):
    racun_stavke = {}
    racun_broj = f'R-{brojac_racuna}-2023-06'
    racun_datum_izdavanja = input(
        'Upišite datum izdavanja računa formata "31.05.2023:\t')

    while True:
        proizvod = input('Upišite naziv proizvoda ')
        cijena = float(input('Upišite cijenu proizvodaq '))
        racun_stavke[proizvod] = cijena
        if not input('Unos nove stavke? Za prestanak pritisnite ENTER '):
            break

    racun = Racun(racun_broj, racun_datum_izdavanja, racun_stavke, pdv)
    return racun


racuni = []
PDV = 0.25

brojac_racuna = 1

while True:

    racun = kreiraj_racun(brojac_racuna, PDV)
    brojac_racuna += 1

    racuni.append(racun)

    if not input('Unos novog RAČUNA? Za prestanak pritisnite ENTER '):
        break

for r in racuni:
    r.ispisi_racun()


racun1 = Racun()


neke_moje_stavke = {'Laptop': 1500.00,
                    'Torba za laptop': 300.00,
                    'Monitor': 550.50,
                    'Python za pocetnike': 23.77}

r1 = Racun('R-1-2023-06', '21.06.2023', neke_moje_stavke, 0.25)

# print(r1.racun_ukupan_iznos)

# print(r1.izracunaj_pdv(r1.racun_ukupan_iznos))
