# ZADATAK: Napisati program koji provjerava je li unesena riječ PALINDROM.

# rijec = input('Upišite riječ za koju želite provjeriti je li palindrom:')

# obrnuta_rijec = rijec[ : : -1]

# if obrnuta_rijec == rijec:
#     print(f'Unesena rijec {rijec} je palindrom!')
# else:
#     print(f"Unesena rijec {rijec} nije palindrom!")

# ZADATAK: Preraditi gornji kod tako da se provjera vrši pomoću korisnički definirane funkcije!

def palindrom(rijec):
    obrnuta_rijec = rijec[ : : -1].upper()

    if obrnuta_rijec == rijec.upper():
        print(f'Unesena rijec {rijec} je palindrom!')
    else:
        print(f"Unesena rijec {rijec} nije palindrom!")

# Poziv funkcije:
palindrom('Ana')
