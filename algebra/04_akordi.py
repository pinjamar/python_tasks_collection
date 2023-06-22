# ZADATAK: Napisati program koji kreira akorde na osnovu početnog tona

# Glazbena abeceda: C, C#, D, D#, E, F, F#, G, G#, A, A#, H

# Durski akord čine: početni ton, 4. ton te 7. ton.
        # Označava se samo velikim slovom početnog tona ili velikim slovom početnog tona uz dodatak dur
        # G# - simbol akorda je G# ili G#
# Molski akord čine: početni ton, 3. ton te 7. ton.
        # Označava se samo malim slovom početnog tona ili malim slovom početnog tona uz dodatak mol
        # G# - simbol akorda je g# ili g#

tonovi = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

print('\nLista svih tonova od tona C:')
for ton in tonovi:
    print(ton, end = ' ')
print('\n')

pocetni_ton = input('Unesite početni ton akorda:\t')

tonovi.extend(tonovi)

indeks_pocetnog_tona = tonovi.index(pocetni_ton)

print(f'\nDurski akord {pocetni_ton} tona čine:\n'
      f'\t{pocetni_ton} kao prvi ton,\n'
      f'\t{tonovi[indeks_pocetnog_tona + 4]} kao 4. ton te\n'
      f'\t{tonovi[indeks_pocetnog_tona + 7]} kao 7. ton.\n'
      f'\tSimbol akorda je: {pocetni_ton} ili {pocetni_ton} dur\n')

print(f"Molski akord od {pocetni_ton}:\n"
      f"\t{pocetni_ton} kao prvi ton, \n"
      f"\t{tonovi[indeks_pocetnog_tona + 3]} kao 3. ton\n"
      f"\t{tonovi[indeks_pocetnog_tona + 7]} kao 7. ton.\n"
      f"\tSimbol akorda je: {pocetni_ton.lower()} ili {pocetni_ton.lower()} mol\n")





