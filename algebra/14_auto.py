# ZADATAK: Kreirajmo klasu Auto koja će sadržavati neke specifične atribute i metode !

class Auto:
    def __init__(self, proizvodac, model, godina):
        self.proizvodac = proizvodac
        self.model = model
        self.godina = godina
        self.prijedeni_kilometri = 0

    def dohvati_detaljni_opis(self):
        print(f'Karakteristike auta su: {self.proizvodac}, {self.model}, {self.godina}')

    def ocitaj_kilometrazu(self):
        print(f'Ovaj auto ima {self.prijedeni_kilometri} prijeđenih kilometara.')

    def napuni_tank_benzina(self):
        print('Tank benzina uspješno napunjen!')

    def azuriraj_kilometrazu(self, udaljenost_u_km):
        self.prijedeni_kilometri = udaljenost_u_km

    def povecaj_kilometrazu(self, km):
        if km <= 0:
            print('Ne možete smanjivati kilometrazu')
        else:
            self.prijedeni_kilometri += km

class ElektricniAuto(Auto):
    def __init__(self, proizvodac, model, godina, velicina_baterije):
        super().__init__(proizvodac, model, godina)
        self.velicina_baterije = velicina_baterije

    def opisi_bateriju(self):
        print(f"Ovaj auto ima {self.velicina_baterije}-kWh bateriju.")
    
    def napuni_tank_benzina(self):
        print('Ovaj auto ne podržava benzin!')

VW = Auto('Volkswagen', 'Golf 5', '2008')
elektricni_auto = ElektricniAuto('Tesla', 'El Tes', '2022', 40)
VW.napuni_tank_benzina()
elektricni_auto.napuni_tank_benzina()

# elektricni_auto.opisi_bateriju()

# elektricni_auto.dohvati_detaljni_opis()
# print(VW.prijedeni_kilometri)
# VW.prijedeni_kilometri = 100000
# print(VW.prijedeni_kilometri)
# VW.azuriraj_kilometrazu(1000)
# print(VW.prijedeni_kilometri)
# VW.povecaj_kilometrazu(-100)
# print(VW.prijedeni_kilometri)
# print(VW.proizvodac)
# print(VW.godina)ž
# VW.napuni_tank_benzina()
# VW.dohvati_detaljni_opis()

# 1. ZADATAK 
# Neka vaša klasa Auto sadrži sljedeće atribute koji se dodjeljuju odmah nakon inicijalizacije objekta:
                # godina_proizvodnje
                # proizvodac
    	        # model


# Za testiranje: Inicijalizirajte objekt autic i s nekim atributima i probajte isprintati te atribute

# 2. ZADATAK
# Kreirajte metodu dohvati_detaljni_opis, koja će, kada se pozove, isprintati rečenicu oblika:
        # Karakteristike auta su: {godina} {prozvodač} {model} 
        # (npr. Karakteristike auta su: 2021 AUDI A4)

# 3. ZADATAK
# Neka se prilikom inicijalizacije objekta, objekt dodijeli još jedan atribut prijedeni_kilometri koji ima vrijednost 0

# 4. ZADATAK
# Kreirajte metodu ocitaj_kilometrazu koja kad se pozove isprinta rečenicu oblika:
    # Ovaj auto ima {} prijeđenih kilometara 
# Kreirajte metodu napuni_tank_benzina koja kad se pozove vrati poruku:
    # Tank benzina uspješno napunjen!

# 5. ZADATAK
# Isprobajte direktno modificirati iznos prijedenih kilometara, nakon što inicijalizirate objekt postavite direktno neku vrijednost
# kilometara koristeći sintaksu: objekt.atribut = zeljena_vrijednost i isprintajte tu novu vrijednost

# 6. ZADATAK
# Kreirajte metodu azuriraj_kilometrazu koja prima udaljenost u km kao parametar i mijenja atribut prijedeni_kilometri

# 7. ZADATAK
# Kreirajte metodu povecaj_kilometrazu koja ce vec postojecu kilometratu povecati za iznos koji predamo toj metodi
# npr. ako nam je trenutna vrijednost prijedeni_kilometri = 100, kad pozovemo metodu povecaj_kilometrazu(100), novi iznos atributa
# prijedeni_kilometri mora postati 200
# Također, zabranite da se kilometraza smanjuje, smije se samo povecavati!

# 8. ZADATAK
# Kreirajte child klasu ElektricniAuto koja ima sve atribute kao i klasa Auto plus dodatno atribut velicina_baterije (npr. 40 kWh) i
# ima metodu opisi_bateriju koja kad se pozove ispise recenicu: Ovaj auto ima {}-kWh bateriju.

# 9. ZADATAK
# Overrideajte metodu napuni_tank_benzina tako da kada se pozove na instanci od električnog auta vrati poruku:
# Elektricni auti ne mogu se napuniti benzinom 

# 10. ZADATAK 
# Instanca kao atribut !!!!

class Auto:
    def __init__(self, proizvodac, model, godina):
        self.proizvodac = proizvodac
        self.model = model
        self.godina = godina
        self.prijedeni_kilometri = 0

    def dohvati_detaljni_opis(self):
        print(f'Karakteristike auta su: {self.proizvodac}, {self.model}, {self.godina}')

    def ocitaj_kilometrazu(self):
        print(f'Ovaj auto ima {self.prijedeni_kilometri} prijeđenih kilometara.')

    def napuni_tank_benzina(self):
        print('Tank benzina uspješno napunjen!')

    def azuriraj_kilometrazu(self, udaljenost_u_km):
        self.prijedeni_kilometri = udaljenost_u_km

    def povecaj_kilometrazu(self, km):
        if km <= 0:
            print('Ne možete smanjivati kilometrazu')
        else:
            self.prijedeni_kilometri += km

class ElektricniAuto(Auto):
    def __init__(self, proizvodac, model, godina, baterija):
        super().__init__(proizvodac, model, godina)
        self.baterija = baterija
    
    def napuni_tank_benzina(self):
        print('Ovaj auto ne podržava benzin!')

class Baterija:
    def __init__(self, velicina_baterije=40):
        self.velicina_baterije = velicina_baterije

    def opisi_bateriju(self):
        print(f"Ovaj auto ima {self.velicina_baterije}-kWh bateriju.")

baterija_obj = Baterija(100)

elektricni_auto = ElektricniAuto('Tesla', 'El Tes', '2022', baterija_obj)

elektricni_auto.baterija.opisi_bateriju()

print(elektricni_auto.baterija.velicina_baterije)
