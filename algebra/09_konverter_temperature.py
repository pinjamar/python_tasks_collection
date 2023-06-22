# ZADATAK: Napravite funkcije koja uzima neku vrijednost temperature i korisnik bira iz koje jedinice pretvara u koju !

# C u F -> C * 1.8 + 32
# C u K -> C + 273.15

# F u C -> (F - 32) / 1.8
# F u K -> (F + 459.67) * 1.8

# K u C -> K - 273.15
# K u F -> K * (9/5) - 459.67

def konverter_temperature(vrijednost, ulazna_mjerna_jedinica, izlazna_mjerna_jedinica):
    """
    Funkcija koja prima vrijednost temperature, ulaznu_mjernu_jedinicu, izlaznu_mjernu_jedinicu i vraća vrijednost
    temperature u izlaznoj mjernoj jedinici
    vrijednost - vrijednost temperature u ulaznoj mjernoj jedinici
    ulazna_mjerna_jedinica - tip temperature u kojoj je vrijednost, a može biti C, K, F
    izlazna_mjerna_jedinica - tip temperature koji može biti C, K, F, a izlaz funkcije mora biti vrijednost temp. u toj jedinici
    """

    if ulazna_mjerna_jedinica == 'C':
        if izlazna_mjerna_jedinica == 'F':
            return vrijednost * 1.8 + 32
        elif izlazna_mjerna_jedinica == 'K':
            return vrijednost + 273.15
        else:
            return vrijednost
    
    elif ulazna_mjerna_jedinica == 'F':
        if izlazna_mjerna_jedinica == 'C':
            return (vrijednost - 32) / 1.8
        elif izlazna_mjerna_jedinica == 'K':
            return (vrijednost + 459.67) * 5/9
        else:
            return vrijednost
    elif ulazna_mjerna_jedinica == 'K':
        if izlazna_mjerna_jedinica == 'C':
            return vrijednost - 273.15
        elif izlazna_mjerna_jedinica == 'F':
            return vrijednost * 9 / 5 - 459.67
    else:
        return vrijednost

iznos_pretvorbe = konverter_temperature(273.15, 'K', 'F') 
print(iznos_pretvorbe)
