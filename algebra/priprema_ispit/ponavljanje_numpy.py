import numpy as np

ocjene = [5, 4, 3, 5, 2]

np_ocjene = np.array([5, 4, 3, 5, 2])

prosjecna_ocjena = np.mean(np_ocjene)

# print(f"Prosjek ocjena: {prosjecna_ocjena}")

# ZADATAK: Kreiraj NumPy niz s 10 nasumičnih decimalnih brojeva između 0 i 1. 
# Zatim, koristeći NumPy funkcije, izračunaj neke statističke vrijednosti

niz = np.random.rand(10)

# print(np.mean(niz))
# print(np.median(niz))
# print(np.std(niz))
# print(np.var(niz))

# ZADATAK Stvori dvije matrice dimenzija 3x3 (možeš koristiti np.random.rand za generiranje slučajnih brojeva)
#  te ih zatim pomnoži (matematički produkt). 
# Nakon toga, izračunaj sumu svih elemenata u rezultirajućoj matrici.

matrica_1 = np.random.rand(3, 3)
matrica_2 = np.random.rand(3, 3)

matrica_final = np.dot(matrica_1, matrica_2)

print(matrica_final)

suma_elemenata = np.sum(matrica_final)

print(suma_elemenata)