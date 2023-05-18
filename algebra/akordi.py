# Napisati program koji kreira akorde na osnovu početnog akorda

# Glazbena abeceda: C, C#, D, D#, E, F, F#, G, G#, A, A#, H

# Durski akord čine: početni ton, 4. ton te 7. ton.
# Označava se samo velikim slovom početnog akorda ili velikim slovom početnog akorda uz dodatak dur

# Molski akord čine: početni ton, 3. ton te 7. ton.
# Označava se samo malim slovom početnog akorda ili malim slovom početnog akorda uz dodatak mol

tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]

prvi_ton = input("Unesi pocetni ton: ")

prvi_index = tonovi.index(prvi_ton)

drugi_index_dur = (prvi_index + 4) % len(tonovi)

treci_index_dur = (drugi_index_dur + 3) % len(tonovi)

print("Durski akord:")
print(tonovi[prvi_index], end=" ")
print(tonovi[drugi_index_dur], end=" ")
print(tonovi[treci_index_dur])


drugi_index_mol = (prvi_index + 3) % len(tonovi)

treci_index_mol = (drugi_index_mol + 4) % len(tonovi)

print("Molski akord:")
print(tonovi[prvi_index], end=" ")
print(tonovi[drugi_index_mol], end=" ")
print(tonovi[treci_index_mol])


# ALTERNATIVE

akordi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]

print("\nLista svih akorda od akorda C:")
for i in akordi:
    print(i, end=" ")

print()

pocetni_akord = input("Unesite pocetni akord:\t")

akordi.extend(akordi)

indeks_pocetnog_akorda = akordi.index(pocetni_akord)

print(f"\nDurski akord {pocetni_akord} cine:\n"
      f"\t{pocetni_akord} kao prvi akord,\n"
      f"\t{akordi[indeks_pocetnog_akorda + 4]} kao 4. akord te\n"
      f"\t{akordi[indeks_pocetnog_akorda + 7]} kao 7. akord\n"
      f"\tSimbol akorda je: {pocetni_akord} ili {pocetni_akord} dur\n")
