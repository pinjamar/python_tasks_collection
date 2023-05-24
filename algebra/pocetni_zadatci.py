import time
print("Hello world from Visual Studio Code!")

################################
ime = "navi"
prezime = "perez"
godina_rodj = 1991
drzava = "rvacka"
zaposlen = True
masa = 100
spol = "M"

print(ime, prezime, godina_rodj, drzava, zaposlen, masa, spol)

################################

a = 10
be = 5

povrsina = a * be

print("pravokutnik stranica", a, "i", be, "ima povrsinnu", povrsina)

################################

# opcija flush u naredbi print, po defaultu flush = False


print("\nIspis Dobra vecer uz flush = True\n")
print("Dobra", end=" ", flush=True)
time.sleep(2)
print("vecer")

print("\nIspis Dobra vecer uz flush = False\n")
print("Dobra", end=" ", flush=False)
time.sleep(2)
print("vecer")

################################
# Docstring (dokumentacijski kod) pise se unutar trostrukih navodnika, na pocetku bilo da je rijec o funkciji, metodi, klasi ili modulu

# primjer docstring kod funkcije


def povrsinaPravokutnika(a, b):
    '''Funkcija povrsinaPravokutnika za pravokutnik s duljinama stranica a i b vraca njenu povrsinu'''
    povrsina = a * b
    return povrsina


x = 5
y = 7

print('pravokutnik sa stranicama a=', x, 'i b=', y,
      'ima povrsinu', povrsinaPravokutnika(x, y), '\b. \n')

# ispis dokumentacijskog koda iz funkcije povrsinaPravokutnika

print(povrsinaPravokutnika.__doc__)

################################
cijena_goriva = float(input("Upišite cijenu goriva: "))

potrosnja_l_po_100km = float(
    input("Unesite prosjecnu potrosnju vaseg auta poo 100km: "))

trosak_km_voznje = potrosnja_l_po_100km / 100

udaljenost_posla = float(
    input("Unesite udaljenost od kuce do posla u jenodm smjeru: "))

vremenski_period = int(input(
    "Navedite za koji vremenski period zelite izracunati potrosnju u kunama: "))

potrosnja = 2.0 * udaljenost_posla * \
    trosak_km_voznje * vremenski_period * cijena_goriva

print(potrosnja)

################################

a = int(input('Upisite prvi broj: '))
b = int(input("Upisite drugi broj: "))

zbroj = a + b

razlika = a - b

umnozak = a * b

kolicnik = a / b

potencija = a ** b

modulo = a % b

print(a, "+", b, "=", zbroj)
print(a, "-", b, "=", razlika)
print(a, "*", b, "=", umnozak)
print(a, "**", b, "=", potencija)
print(a, "%", b, "=", modulo)

################################
# ip adresa = 192.168.0.184

prvi_oktet = bin(192)
drugi_oktet = bin(168)
treci_oktet = bin(0)
cetvrti_oktet = bin(184)

print(prvi_oktet, drugi_oktet, treci_oktet, cetvrti_oktet, sep=".")

prvi_oktet_o = oct(192)
drugi_oktet_o = oct(168)
treci_oktet_o = oct(0)
cetvrti_oktet_o = oct(184)

print(prvi_oktet_o, drugi_oktet_o, treci_oktet_o, cetvrti_oktet_o, sep=".")

################################
ime = "Filp"
prezime = "Skenderovic"
puno_ime = "Puno ime i prezime je: {} {}".format(ime, prezime)

print(puno_ime)
