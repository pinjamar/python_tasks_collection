class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, brzina = 0):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.brzina = brzina

    def prikazi_podatke(self):
        print(f"Značajke automobila: {self.marka}, {self.model}, {self.godina_proizvodnje}, {self.brzina}")

    def ubrzaj(self, iznos):
        self.brzina += iznos
        print(f'Brzina je uvećana za {iznos} km/h i trenutno iznosi {self.brzina} km/h')

    def koja_brzina(self):
        print(self.brzina)

    def zaustavi(self):
        self.brzina = 0

class ElektricniAutomobil(Automobil):
    def __init__(self, marka, model, godina_proizvodnje, domet, brzina=0):
        super().__init__(marka, model, godina_proizvodnje, brzina)
        self.domet = domet
    
    def prikazi_domet(self):
        print(self.domet)

elektricni_automobil = ElektricniAutomobil('Tesla', 'Tesla Model', '2022', 200)

elektricni_automobil.prikazi_podatke()
elektricni_automobil.prikazi_domet()

