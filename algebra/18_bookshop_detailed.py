
# Kada radimo s ORM sustavima onda imamo koncept modela.
# Model predstavljamo pomocu klase koja ima je reprezentacija tabele u bazi.
# Na ovaj nacin radimo uvijek u jednom programskom jeziku.

# Kreirajmo modele za knjige, autore i izdavace za nas Bookshop

### 1. KORAK ###
# Kada god zelimo raditi s SQLAlchemy trebamo uključiti sqlalchemy
# Ali nam trebaju i jos neki moduli SQLAlchemy paketa nuzni za kreiranje klasa
# koje ce sluziti kao predlozak za tabele u bazi
import sqlalchemy as db
from sqlalchemy.orm import relationship, backref, declarative_base, sessionmaker

# Kreirajmo objekt Baza koja predstavlja posrednika izmedu klasa modela i tabela u bazi
Base = declarative_base()

# Many-To-Many relacija autor-izdavaci - svaki autor moze imati vise izdavaca i obratno
# primjer tablice: 
    	# autor_id  izdavac_id
        #   1           1
        #   2           2
        #   1           2
        #   3           1
        #   3           3

autor_izdavac = db.Table(
    "autor_izdavac",
    Base.metadata,
    db.Column("autor_id", db.Integer, db.ForeignKey("autor.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id")),
)

# Many-To-Many relacija knjiga-izdavaci
knjiga_izdavac = db.Table(
    "knjiga_izdavac",
    Base.metadata,
    db.Column("knjiga_id", db.Integer, db.ForeignKey("knjiga.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id")),
)

# VAZNO je nasljedivanje Base klase
class Autor(Base):
    __tablename__ = "autor"
    # Stupac naziva id, tip je broj i to je primarni kljuc
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String)
    prezime = db.Column(db.String)
    # Gornja tri stupca predstavljaju "stvarne" kolone u našoj tablici autor u bazi proba.db

    # Definirajmo relacije!

    # Svaki autor ima kolekciju knjiga 'knjige' u kojoj su podaci definirani u klasi Knjiga
    # Klasa "Knjiga" (prvi argument u relationship funkciji) imat ce povratnu referencu 'bekref' na tablicu autor - 1-To-Many relacija
    # Dakle, argument "autor" koji se nalazi unutar backref funkcije predstavlja zapravo "pseudo" kolonu
    # koja postoji u knjiga tablici pa kad niže instancirate objekt iz klase Knjiga, možete predati i autor
    # parametar.
    # Ako provjerite ispod vidjet ćete da fizički nemamo prisutnu autor kolonu

    knjige = relationship("Knjiga", backref=backref("autor"))

    # Many-To-Many relacija autor-izdavaci - svaki autor moze imati vise izdavaca i obratno
    # Najprije što želimo napraviti je povezati te dvije tablice, a to ćemo napraviti tako da kreiramo jednu
    # međutablicu koja će sadržavati samo id-eve od autora i izdavača (vidi iznad: autor_izdavac)
    # Dakle, kreiramo novu varijablu izdavaci koja predstavlja sve izdavače s kojima je autor povezan
    izdavaci = relationship(
        "Izdavac", secondary=autor_izdavac, back_populates="autori" # ovdje nam je sad "autori" pseudo kolona koja
                                                             # se kreira u Izdavac tablici u kojoj čuvamo
                                                             # sve autore s kojima surađuje neki izdavac
    )
    # NAPOMENA: ovdje se koristi backref, a ne back_populates kao na predavanju, može i jedno i drugo 
    # Dakle, možemo razmišljati o backref kao stavljanje "fake" kolone u tsblicu s kojom imamo neku relaciju
    # (u ovom slučaju imamo relaciju s izdavačima pa stavljamo lažnu kolonu u izdavac tablicu)

    def __repr__(self):
        return f'<Autor: {self.ime} {self.prezime}>'
    
class Knjiga(Base):
    __tablename__ = "knjiga"
    id = db.Column(db.Integer, primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"))
    naslov = db.Column(db.String)
    izdavaci = relationship(
        "Izdavac", secondary=knjiga_izdavac, back_populates="knjige"
    )

    def __repr__(self):
        return f'<Knjiga: {self.naslov}>'

class Izdavac(Base):
    __tablename__ = "izdavac"
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String)
    autori = relationship(
        "Autor", secondary=autor_izdavac, back_populates="izdavaci"
    )
    knjige = relationship(
        "Knjiga", secondary=knjiga_izdavac, back_populates="izdavaci"
    )

    def __repr__(self):
        return f'<Izdavac: {self.naziv}>'

# Dolje je na nekoliko primjera demonstrirano kako radi ovaj način referenciranja

###### 1. Primjer ######

# # Kreirat ćemo autora, isti je postupak kao i kad instanciramo objekt iz neke obične klase
# jkrowling = Autor(ime = 'Joanne', prezime = 'Rowling')

# # Možemo najnormalnije pristupati atributima autora jkrowling:
# print(jkrowling.ime)
# print(jkrowling.prezime)

# # Zbog __repr__ funkcije možemo i isprintati cijeli objekt i dobiti ljepši ispis
# print(jkrowling)

# # Kreirajmo knjigu:
# # harrypotter = Knjiga(naslov = 'Kamen Mudraca')

# # Provjerite sad tablicu knjiga i tablicu autor i obratite pažnju u tablici knjiga na kolonu autor_id, ona je NULL
# # Ona je null jer nismo uspostavili nikakvu konekciju između autora i knjige, a u definiciji knjige je navedeno
# # da je autor_id foreign key koji gleda na autor.id kolonu. Trenutno knjiga ne zna na koji id mora gledati

# # OBRIŠITE BAZU I ZAKOMENTIRAJTE harrypotter LINIJU! OTKOMENTIRAJTE 130. liniju

# # Sad možemo kreirati i knjigu kojoj ćemo dodati autora (koristimo lažnu kolonu u tablici knjiga 
# # pod nazivom "autor")

# harrypotter = Knjiga(naslov = 'Kamen Mudraca', autor = jkrowling) 

# # Provjerite sad tablicu knjiga i tablicu autor
# # Sad u tablivi knjiga imamo autor_id jer smo uspostavili relaciju između knjige i autora.
# # Isto tako sad možemo isprintati autora knjige harrypotter:

# # print(harrypotter.autor)
# db_engine = db.create_engine("sqlite:///proba.db")

# # Kreiraj bazu po uputama koje su gore navedene
# Base.metadata.create_all(db_engine)


# Session = sessionmaker()
# Session.configure(bind=db_engine)
# session = Session()

# session.add(jkrowling)
# session.add(harrypotter)


# session.commit()

###### 2. Primjer ######

# ZAKOMENTIRAJTE SVE IZ 1.  PRIMJERA I OBRIŠITE BAZU

# Kreirat ćemo dva autora i tri izdavača, isti je postupak kao i kad instanciramo objekt iz neke obične klase
izvor = Izdavac(naziv = 'izvori')
mozaik = Izdavac(naziv = 'mozaik')
skolska_knjiga = Izdavac(naziv = 'skolska_knjiga')

# jkrowling = Autor(ime = 'Joanne', prezime = 'Rowling')
pcoelho = Autor(ime = 'Paulo', prezime = 'Coelho')

# Zakomentirajte kod ispod i pokrenite kod iznad i
# Provjerite sad tablicu autor i tablicu izdavac i njihovu međutablicu
# Međutablica je prazna, jer nismo uspostavili nikakvu relaciju između ovih objekata

# Zakomentirajte jkrowling iznad i dodajmo sad izdavace autoru jkrowling:
jkrowling = Autor(ime = 'Joanne', prezime = 'Rowling', izdavaci = [izvor, mozaik])

# Zakomentirajte sve ispod osim pokretanja konekcije i sesije i pokrenite kod
# Provjerite sad sadržaj tablica i međutablice autor_izdavač
# Možemo sad dodati i jkrowling autoru još jednog izdavača nakon što smo već instacirali taj objekt:
jkrowling.izdavaci.append(skolska_knjiga)

# Pokušajte drugom autoru dodati neke izdavače
#
#
#
#
#

# Možemo najnormalnije isprintati izdvača autora jkrowling:
print(jkrowling.izdavaci)

# Dobijemo listu pa možemo raditi sve naredbe koje i inače radimo s listama
for izdavac in jkrowling.izdavaci:
    print(izdavac.naziv)
    # Lista se sastoji od objekata izdavac koji imaju atribute naziv, autori, knjige

db_engine = db.create_engine("sqlite:///proba.db")

# Kreiraj bazu po uputama koje su gore navedene
Base.metadata.create_all(db_engine)


Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()

session.add(jkrowling)
session.add(mozaik)
session.add(izvor)
session.add(skolska_knjiga)

session.commit()

## DODAJTE JOŠ NEKOLIKO KNJIGA, AUTORA I IZDAVAČA i poigrajte se s razno raznim kombinacijama. 