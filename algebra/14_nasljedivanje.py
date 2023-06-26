### SLUČAJ 1 ###
# Kreirajmo klasu osoba koja ima svojstva ime, oib i adresa

class Osoba:
    def __init__(self, ime, oib, adresa):
        
        self.ime = ime
        self.oib = oib
        self.adresa = adresa
    
# Kreirajmo klasu tvrtka - pravna osoba
class Tvrtka:
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik = ''):
        
        self.ime = ime
        self.oib = oib
        self.adresa = adresa
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik

# Kreirajmo klasu za čuvanje podataka o Djelatniku Tvrtke
class Djelatnik:
    def __init__(self, ime, oib, adresa, radno_mjesto):
        
        self.ime = ime
        self.oib = oib
        self.adresa = adresa
        self.radno_mjesto = radno_mjesto

# Želimo promijeniti naziv svojstva oib u OIB ili vat_hr ili nešto treće
# Postoji opasnost da ćemo to svojstvo zaboraviti preimenovati u nekoj od klasa !

# Vidimo da se neka svojstva ponavljaju (ime, oib, adresa)
# Ne želimo unutar djelatnik ili tvrtka opet ponavljati svojstva koja su definirana u OSOBI jer su i one same neki tip osobe 
# Ovdje nam nastupa INHERITANCE (NASLJEĐIVANJE)

# Kreirajmo klasu za čuvanje podataka o djelatniku tvrtke
class Djelatnik(Osoba):
    def __init__(self):
        super().__init__()
        self.radno_mjesto = 'Direktor'

# Kreirajmo klasu za čuvanje podataka o tvrtki
class Tvrtka(Osoba):
    def __init__(self):
        super().__init__()
        self.broj_djelatnika = 25
        self.pravni_oblik = 'd.d.'

# Metoda super() predstavlja poziv konstruktora klase koju se nasljeđuje, u našem slučaju klase Osoba
# Mi ustvari kreiramo još jedan objekt tipa Osoba i povežemo s drugim objektom tipa Tvrtka.

# NAPOMENA: Ako PARENT (u našem slučaju OSOBA) ne koristi konstruktor, onda u klasi koja je nasljeđuje nema potrebe koristiti
# metodu super() 

# Što kada klasa ima konstruktor koji prima neke vrijednosti??

class Osoba:
    def __init__(self, ime, oib, adresa):
        self.oib = oib
        self.adresa = adresa
        self.ime = ime
    
    def print_name(self):
        print(self.ime)

# Kreirajmo klasu tvrtka 
class Tvrtka(Osoba):
    # Prvo klasa Tvrtka preuzme sve vrijednosti i onda ih po potrebi rasporedi
    # Jedan dio ide za vlastita specifična svojstva, a drugi se proslijeđuje u konstruktor Parent klase
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        super().__init__(ime, oib, adresa)
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik

class Djelatnik(Osoba):
    def __init__(self, ime, oib, adresa, radno_mjesto):
        super().__init__(ime, oib, adresa)
        self.radno_mjesto = radno_mjesto

d = Djelatnik('Petar Perić', '12345678900', 'Adresa Nad Lipom 35', 'šljaker')

print(d.oib)

d.print_name()
# Kod djelatnika i tvrtke je oib naziv proizvoljan -> on je povezan s varijablom koju prosljeđujemo !
