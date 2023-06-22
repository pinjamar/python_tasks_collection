# ZADATAK: Kreirajte funkciju koja prima rečenicu i vraća broj uppercase, odnosno lowercase znakova u toj rečenicu. Sve ostale znakove zanemaruje.

# Ukupan broj lower, odnos uppercase znakova pohranite u dict, koji je definiran unutar same funkcije!

# HINT: Koristite gotovu funkciju isupper() -> vraća boolean, True ako je uppercase, False inače
# character.isupper()

def case_counter(sentence):
    d = {'UPPER_CASE': 0, 'LOWER_CASE': 0}
    for character in sentence:
        if character.isupper():
            d['UPPER_CASE'] += 1
        elif character.islower():
            d['LOWER_CASE'] += 1
        else:
            pass
    print('Ovo se izvršilo unutar funkcije')
    print(d)
    return d

moj_rjecnik = case_counter('Programiranje u Pythonu - Algebra')
print('Izvršavamo nakon funkcije')
print(moj_rjecnik)

# 'Programiranje u Pythonu - Algebra'
# imamo rječnik d i imamo key UPPER_CASE i želimo povećati value za 1 !