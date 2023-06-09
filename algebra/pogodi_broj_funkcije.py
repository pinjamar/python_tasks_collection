### POGODI BROJ ###
# Sjećate se Računalnog razmišljanja i pogađanja broja između 1 i 100. Sada imate dovoljno znanja da napišete
# program koji će Vam omogućiti pogađanje broja
import random



# a = vrati_slucajni_broj()

# print('U varijablu a smo pohranili broj:')
# print(a)

# b = vrati_slucajni_broj()

# print('U varijablu b smo pohranili broj:')
# print(b)

# print("Zbroj a + b je:")
# print(a + b)

# print()

# def pozdrav_svijetu():
#     tekst = "Hello, world!"
#     return tekst

# recenica = pozdrav_svijetu()
# print(recenica)

def vrati_slucajni_broj():
    slucajni_broj = random.randint(1, 100) # Od 1 do 100 UKLJUČIVO - nije isto kao range()
    return slucajni_broj

def pogodi_broj():

    slucajni_broj = vrati_slucajni_broj()

    broj_pokusaja = 0
    while True:
        # Ovu liniju koristiti samo tijekom testiranja, kasnije izbrisati ili komentirati
        print('Zamišljeni broj:', slucajni_broj)
        print()
        odgovor = input('Pogodi broj od 1 do 100 koji sam zamislio.\t')
        broj_pokusaja += 1
        
        # NE smijemo zaboraviti broj pretvoriti u broj
        if int(odgovor) == slucajni_broj:
            print()
            print('ČESTITAM! To je taj broj koji sam zamislio.')
            print(f'Za to ti je trebalo {broj_pokusaja} pokušaja!')
            print()
            break
        elif int(odgovor) > slucajni_broj:
            print(f'Broj je manji od {odgovor}')
        elif int(odgovor) < slucajni_broj:
            print(f'Broj je veći od {odgovor}')

pogodi_broj()