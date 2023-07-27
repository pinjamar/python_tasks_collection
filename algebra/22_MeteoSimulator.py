from sense_emu import SenseHat

sense = SenseHat()

# Sad kad imamo sense objekt, možemo dohvatiti očitane vrijednosti temperature,
# vlažnosti i tlaka

# Najjednostavnije je kreirati varijablu za svaku od tih veličina

temperature = sense.get_temperature()

# Ovaj put ćemo provjeriti što smo dobili i to prikazati u konzoli
# print(temperature)

temperature_from_humidity = sense.get_temperature_from_humidity()
temperature_from_pressure = sense.get_temperature_from_pressure()

# print(temperature_from_humidity)
# print(temperature_from_pressure)

# Ako pomaknemo slider za temperaturu na Sense HAT Emulatoru dobit ćemo druge vrijednosti.

# Očitajmo tlak zraka
tlak = sense.get_pressure()
# print(tlak)

# Očitajmo sad i vlažnost zraka
vlaznost = sense.get_humidity()
# print(vlaznost)

# Zaokružimo sve rezultate na jednu decimalu

temperature = round(sense.get_temperature(), 1)
tlak = round(sense.get_pressure(), 1)
vlaznost = round(sense.get_humidity(), 1)

print(f'Temperatura je {temperature}°C, tlak zraka je {tlak} mbar-a, a vlažnost je {vlaznost} %')

# ZADATAK:
"""
Potrebno je očitati temperaturu, tlak i vlaznost zraka sa senzore i prikazati ih na ekranu
tako da kad god se poveća vrijednost prvo se prikaže bijela strelica na crvenoj podlozi
koja se kreće (scroll) prema gore pa nakon toga mjerena veličina i očitana vrijednost.

Kad se vrijednost snizi, onda se koristi plava podloga i kretanje strelice prema dolje.
"""