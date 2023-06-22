# ZADATAK: Napišite funkciju kloja prima rječnik, a ispisuje koji su ključevi rječnika, a koje su vrijednosti rječnika. Za ispis koristite 
# formatirane rečenice

def dict_decomposer(init_dict):
    kljucevi = []
    vrijednosti = []
    for key, value in moj_rječnik.items():
        kljucevi.append(key)
        vrijednosti.append(value)

    print(f'Ključevi rječnika su {kljucevi}')
    print(f'Vrijednosti ključeva su {vrijednosti}')

moj_rječnik = {
    'ime': 'Filip',
    'prezime': 'Skendrovic'
}

dict_decomposer(moj_rječnik)

# rezultat = dict_decomposer(moj_rječnik)
# print(type(rezultat)) # Rezultat će biti: None