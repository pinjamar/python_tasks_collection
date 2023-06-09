# ZADATAK: Napiši program koji će uneseni broj kartice od korisnika zaštititi tako da sve znakove osim zadnja četiri
# maskira pomoću # znakova. Broj kartice mora biti veći od 5.

# PRIMJER: Broj 123456789 treba biti zapisan kao #####6789

# # def sakrij_znakove(tekst):
# #     zasticeni_tekst = ''
# #     if len(tekst) <= 5:
# #         return f'Tekst {tekst} ima 5 ili manje znakova!'
# #     else:
# #         limit_zastite = len(tekst) - 4
# #         indeks = 0
# #         for znak in tekst:
# #             if indeks < limit_zastite:
# #                 zasticeni_tekst += '#'
# #                 indeks += 1
# #             else:
# #                 zasticeni_tekst += znak
# #                 indeks += 1
# #         return zasticeni_tekst
    
# # kartica = input('\nUpišite broj Vaše kreditne kartice:\t')

# # print(f"Nezaštićeni broj vase kartice je {kartica}")

# # print(f"Zašićeni broj kartice je {sakrij_znakove(kartica)}")

##########################################################################################################
# ZADATAK: Modificiraj gornji program tako da zanemaruje - ! Broj kartice mora biti veći od 5.

# PRIMJER: Broj 123456789-3-4-5-6 treba biti zapisan kao #########-3-4-5-6

def sakrij_znakove(tekst):
    zasticeni_tekst = ''
    if len(tekst) <= 5:
        return f'Tekst {tekst} ima 5 ili manje znakova!'
    else:
        brojac = 0
        for znak in tekst[ : : -1]:
            if znak != '-' and brojac < 4:
                zasticeni_tekst += znak
                brojac += 1
            elif znak != '-' and brojac >= 4:
                zasticeni_tekst += '#'
            else:
                zasticeni_tekst += znak

        return zasticeni_tekst[ : : -1]
    
kartica = input('\nUpišite broj Vaše kreditne kartice:\t')

print(f"Nezaštićeni broj vase kartice je {kartica}")

print(f"Zašićeni broj kartice je {sakrij_znakove(kartica)}")
