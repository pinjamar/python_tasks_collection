### KORAK 1 ###
# Definiramo klasu naziva NazivKlase. Korisno je uz klasu dodati docstring.
# Preporuka za nazivanje klasa je da naziv / ime počinje velikim početnim slovom i da se riječi ne odvajaju '_'
# Za naziv klase koristimo CAMELCASE - NazivKlase, KlasaZaDohvatPodatakaIzBazePsi

# slično kao kod funkcija, imamo ključnu riječ ! -> CLASS
class NazivKlase:
    '''
    Docstring koristimo za opis klasa.
    '''
    pass

# Kad smo definirali klasu / predložak nekog tipa podatka / korisnički definirani tip podatka možemo je iskoristiti za 
# kreiranje varijabli / objekata na osnovu te klase

objekt1 = NazivKlase()
objekt2 = NazivKlase()

# pas1 = Dog()
# pas2 = Dog()

# Varijabla objekt1 predstavlja instancu klase NazivKlase !!! 

### KORAK 2 ###
# Kreirat ćemo klasu koja ima neku stvarnu namjenu!

# class TelevizijskiAparat:
#     dijagonala = 55
#     sirina = 124
#     visina = 79
#     proizvodac = 'Grundig'
#     model = 'Ultra Smart Turbo Extra Full HD TV'

#     # Treba nam svojstvo koje čuva stanje je li TV uključen ili nije
#     je_ukljucen = False

#     # Kreirajmo metodu (isto kao što kreiramo i funkcije!)
#     def ukljuci(self):
#         self.je_ukljucen = True

# tv_dnevni_boravak = TelevizijskiAparat()
# tv_skladiste = TelevizijskiAparat()

# print('Status aparata:')
# if (tv_dnevni_boravak.je_ukljucen):
#     print(f'Status; TV aparat u dnevnom boravku JE uključen')
# else:
#     print(f'Status: TV aparat u dnevnom boravku NIJE ukljucen')


# print('Ukljuci tv u dnevnom boravku')
# tv_dnevni_boravak.ukljuci()

# if (tv_dnevni_boravak.je_ukljucen):
#     print(f'Status; TV aparat u dnevnom boravku JE uključen')
# else:
#     print(f'Status: TV aparat u dnevnom boravku NIJE ukljucen')

# me, mySELF and I
# u prijevodu -> self se odnosi na objekt koji je pozvao određenu metodu ili svojstvo
# u primjeru iznad, pomoću self, TV u dnevnom boravku zna da treba SEBI promijeniti svojstvo

### KORAK 3 ### 
# U prethodnim primjerima smo već definirali vrijednosti svojstva unaprijed.
# Klasa je nacrt i ne bi trebala imati predefinirane vrijednosti! 
# Ne želimo koristiti predefinirane vrijednosti !! 
# Koristit ćemo tzv. KONSTRUKTOR
# Pomoću konstruktora osiguravamo da prilikom inicijalizacije (INITialization) objekta, klasi predaju vrijednosti koje će se
# pridružiti svojstvima.

# tv1 = TelevizijskiAparat(55, 150, 70, 'LG', '4K HD', False)

class TelevizijskiAparat:
    # KONSTRUKTOR se piše odmah na početku klase !!
    # U konstruktoru navodimo argumente koje želimo dobiti kod INITijalizacije objekta
    # Također je prvi element self!!!

    def __init__(self, dijagonala, sirina, visina, proizvodac, model, program = 0, glasnoca = 0, je_ukljucen = False): # MAGIC metoda ili DUNDER metode DOUBLE UNDERSCORE
        self.dijagonala = dijagonala # 55
        self.sirina = sirina
        self.visina = visina
        self.proizvodac = proizvodac
        self.model = model
        self.program = program
        self.glasnoca = glasnoca
        self.je_ukljucen = je_ukljucen

    def ukljuci(self):
        print('TV JE UKLJUČEN')
        self.je_ukljucen = True
        self.program = 1
        self.glasnoca = 3
    
    def promijeni_program(self, novi_program):
        self.program = novi_program

    def podesi_glasnocu(self, smjer_promjene = ' ', razina_glasnoce = 3):
        if smjer_promjene == 'glasnije':
            self.glasnoca += 1
        elif smjer_promjene == 'tise':
            self.glasnoca -= 1
        elif smjer_promjene == 'prigusi':
            self.glasnoca = 0
        else:
            self.glasnoca = razina_glasnoce

tv1 = TelevizijskiAparat(55, 150, 70, 'LG', '4K HD')
# tv2 = TelevizijskiAparat(32, 111, 34, 'Samsung', 'ULTRA COOL')
tv1.ukljuci()
# tv2.ukljuci()
# print(tv1.dijagonala)
# print(tv1.program)

# print(tv1.program)

# tv1.promijeni_program(4)

# print(tv1.program)

tv1.podesi_glasnocu()
print(tv1.glasnoca)
