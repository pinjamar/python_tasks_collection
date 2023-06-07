# napisi program koji ce uneseni broj kartice od korisnika zastititi tako da sve znakove osim zadnja cetiri maskira pomocu # znakova
# broj kartice mora biti veci ili jednak 5
# modificiraj program tako da zanemaruje -

# primjer - broj 123456789 treba biti zapisan ######4789
# primjer 324156553-4-5-7-5-2

def sakrij_znakove(tekst):
    zasticeni_tekst = ""
    if len(tekst) <= 5:
        return f'Tekst {tekst} ima 5 ili manje znakova!'
    else:
        limit_zastite = len(tekst) - 4
        indeks = 0
        for znak in tekst:
            if indeks < limit_zastite:
                zasticeni_tekst += "#"
                indeks += 1
            else:
                zasticeni_tekst += znak
                indeks += 1
        return zasticeni_tekst


kartica = input('\nUpisite broj vase kreditne kartice:\t')
print(f'Nezasticeni broj kartice je {kartica}')
print(f'Zasticeni broj kartice je {sakrij_znakove(kartica)}')
