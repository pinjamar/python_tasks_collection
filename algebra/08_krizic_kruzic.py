polje_na_ploci = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def status_igre():
    if polje_na_ploci[1] == polje_na_ploci[2] and polje_na_ploci[2] == polje_na_ploci[3]:
        return 1
    elif polje_na_ploci[4] == polje_na_ploci[5] and polje_na_ploci[5] == polje_na_ploci[6]:
        return 1
    elif polje_na_ploci[7] == polje_na_ploci[8] and polje_na_ploci[8] == polje_na_ploci[9]:
        return 1
    elif polje_na_ploci[1] == polje_na_ploci[4] and polje_na_ploci[4] == polje_na_ploci[7]:
        return 1
    elif polje_na_ploci[2] == polje_na_ploci[5] and polje_na_ploci[5] == polje_na_ploci[8]:
        return 1
    elif polje_na_ploci[3] == polje_na_ploci[6] and polje_na_ploci[6] == polje_na_ploci[9]:
        return 1
    elif polje_na_ploci[1] == polje_na_ploci[5] and polje_na_ploci[5] == polje_na_ploci[9]:
        return 1
    elif polje_na_ploci[3] == polje_na_ploci[5] and polje_na_ploci[5] == polje_na_ploci[7]:
        return 1
    elif (polje_na_ploci[1] != 1 and
          polje_na_ploci[2] != 2 and
          polje_na_ploci[3] != 3 and
          polje_na_ploci[4] != 4 and
          polje_na_ploci[5] != 5 and
          polje_na_ploci[6] != 6 and
          polje_na_ploci[7] != 7 and
          polje_na_ploci[8] != 8 and
          polje_na_ploci[9] != 9):
        return 0
    else:
        return -1
    
def iscrtaj_plocu():
    print()
    print('\t     |     |     ')
    print('\t ', polje_na_ploci[1], ' | ' , polje_na_ploci[2], ' | ' , polje_na_ploci[3])

    print('\t_____|_____|_____')
    print('\t     |     |   ')

    print('\t ', polje_na_ploci[4], ' | ' , polje_na_ploci[5], ' | ' , polje_na_ploci[6])

    print('\t_____|_____|_____')
    print('\t     |     |   ')

    print('\t ' , polje_na_ploci[7], ' | ' , polje_na_ploci[8], ' | ' , polje_na_ploci[9])

    print('\t_____|_____|_____')
    print('\t     |     |   ')

igrac = 1
trenutni_status_igre = -1

while trenutni_status_igre == -1:
    iscrtaj_plocu()

    if igrac % 2 == 1:
        igrac = 1
    else:
        igrac = 2

    print('\n\nIgrac ', igrac)
    izabrano_polje = int(input('Unesite broj polja na ploči:'))

    # mogli smo napraviti funkciju koja će kao parametar primiti odabrano polje i broj igrača i zamijeniti broj u listi
    # s pripadajućim znakom !!
    
    # def update_polja_na_ploci(izabrano_polje, oznaka_igraca, polje_na_ploci):
    #   polje_na_ploci[izabrano_polje] = oznaka_igraca

    # Provjera statusa igre:
    if igrac == 1:
        oznaka_igraca = 'X'
    else:
        oznaka_igraca = 'O'
    
    # update_polja_na_ploci(izabrano_polje, oznaka_igraca, polje_na_ploci)
    
    if izabrano_polje == 1:
        polje_na_ploci[1] = oznaka_igraca
    elif izabrano_polje == 2:
        polje_na_ploci[2] = oznaka_igraca
    elif izabrano_polje == 3:
        polje_na_ploci[3] = oznaka_igraca
    elif izabrano_polje == 4:
        polje_na_ploci[4] = oznaka_igraca
    elif izabrano_polje == 5:
        polje_na_ploci[5] = oznaka_igraca
    elif izabrano_polje == 6:
        polje_na_ploci[6] = oznaka_igraca
    elif izabrano_polje == 7:
        polje_na_ploci[7] = oznaka_igraca
    elif izabrano_polje == 8:
        polje_na_ploci[8] = oznaka_igraca
    elif izabrano_polje == 9:
        polje_na_ploci[9] = oznaka_igraca

    trenutni_status_igre = status_igre()
    igrac += 1

iscrtaj_plocu()
print('\n\nREZULTAT\n')
if trenutni_status_igre == 1:
    print('Igrac ', igrac-1,'je pobijedio!\n\n')
else:
    print('Neriješeno\n\n')