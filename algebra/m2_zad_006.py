cijena_goriva = float(input("Upišite cijenu goriva: "))

potrosnja_l_po_100km = float(input("Unesite prosjecnu potrosnju vaseg auta poo 100km: "))

trosak_km_voznje = potrosnja_l_po_100km / 100

udaljenost_posla = float(input("Unesite udaljenost od kuce do posla u jenodm smjeru: "))

vremenski_period = int(input("Navedite za koji vremenski period zelite izracunati potrosnju u kunama: "))

potrosnja = 2.0 * udaljenost_posla * trosak_km_voznje * vremenski_period * cijena_goriva

print(potrosnja)