# Kada radimo s ORM modelima onda imamo koncept modela
# Model predstavljamo pomoću klase, koja je reprezentacija tablice u bazi
# Ovo je način da radimo uvijek u jednom programskom jeziku!

# Kreirat ćemo modele za knjige, autore i izdavace za nas Bookshop

import sqlalchemy as db
from sqlalchemy.orm import relationship, backref, declarative_base, sessionmaker

# Kreirajmo objekt baza koja predstavlja posrednika između klasa modela i tabela u bazi
Base = declarative_base()

knjiga_izdavac = db.Table(
    "knjiga_izdavac",
    Base.metadata,
    db.Column("knjiga_id", db.Integer, db.ForeignKey("knjiga.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id"))
)

autor_izdavac = db.Table(
    "autor_izdavac",
    Base.metadata,
    db.Column("autor_id", db.Integer, db.ForeignKey("autor.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id"))
)
class Autor(Base):
    __tablename__ = "autor"

    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String)
    prezime = db.Column(db.String)

    # Svaki autor ima više knjiga, ali svaka je knjiga napisana od strane samo jednog autora!
    knjige = relationship("Knjiga", backref=backref("autor"))
    izdavaci = relationship("Izdavac", secondary=autor_izdavac, back_populates="autori")

class Knjiga(Base):
    __tablename__ = "knjiga"

    id = db.Column(db.Integer, primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"))
    naslov = db.Column(db.String)
    izdavaci = relationship("Izdavac", secondary=knjiga_izdavac, back_populates="knjige")

class Izdavac(Base):
    __tablename__ = "izdavac"
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String)
    autori = relationship("Autor", secondary=autor_izdavac, back_populates="izdavaci")
    knjige = relationship("Knjiga", secondary=knjiga_izdavac, back_populates="izdavaci")

jkrowling = Autor(ime = 'Joanne', prezime = 'Rowling')
acamus = Autor(ime = 'Albert', prezime = 'Camus')
izvor = Izdavac(naziv = 'izvori', autori = [jkrowling, acamus])
mozaik = Izdavac(naziv = 'mozaik')

# jkrowling.izdavaci.append(izvor)
# jkrowling.izdavaci.append(mozaik)


harrypotter = Knjiga(naslov = 'Kamen Mudraca', autor = jkrowling)
cudesnezvijeri = Knjiga(naslov = 'Cudesne Zvijeri', autor = jkrowling)

print(jkrowling.ime)
print(jkrowling.knjige)
print(jkrowling.izdavaci)

for izdavac in jkrowling.izdavaci:
    print(izdavac.naziv)

acamus.izdavaci.append(mozaik)
acamus.izdavaci.append(izvor)
print(jkrowling.izdavaci)

db_engine = db.create_engine("sqlite:///proba.db")
Base.metadata.create_all(db_engine)

Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()

session.add(jkrowling)
session.add(harrypotter)
session.add(mozaik)
session.add(izvor)

session.commit()