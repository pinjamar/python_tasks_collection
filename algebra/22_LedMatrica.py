"""
from sense_hat import SenseHat
sense = SenseHat()
"""

from sense_emu import SenseHat
import time

sense = SenseHat()

# sense.show_message('Cestitam, uspjeli ste')

# Želimo da je poruka plave boje. Kreirajmo varijablu plavi koja koristi RGB vrijednosti
# (red, green, blue), 0 označava da je boja isključena, a 255 označava da je dodan
# maksimalan intenzitet boje

plavo = (0, 0, 255)
# sense.show_message('Cestitam, uspjeli ste!', text_colour = plavo)

pozadina = (0, 255, 0)
# sense.show_message('Cestitam, uspjeli ste!',
#                    text_colour = plavo,
#                    scroll_speed = 0.55,
#                    back_colour = pozadina)

# Možemo poruku ponavljati u beskonačnost!
# while True:
#     sense.show_message('Cestitam, uspjeli ste!',
#                    text_colour = plavo,
#                    scroll_speed = 0.05,
#                    back_colour = pozadina)

# Ako imamo show_message, imamo li i show letter?
# while True:
#     sense.show_letter('P',
#                       text_colour=plavo,
#                       back_colour=pozadina)

# Što ako želimo prikazati točku po točku?
# Postoji naredba set_pixel() koja nam to omogućava, prima tri parametra:
    # x koordinata -> od 0 do 7
    # y kooridnata -> od 0 do 7
    # polje koje definira RGB boju
    
sense.set_pixel(0, 2, [0, 0, 255])

# Prikazala nam se crvena točka, ali ostalo nam je i slovo P
# Postoji funkcija clear() koja će nam resetirati LED diode na početne vrijednosti

sense.clear()
sense.set_pixel(0, 2, [0, 0, 255])

# Funkcija clear() je sve LED diode postavila na CRNU boju, odnosno isključila ih je
sense.clear(plavo)
sense.set_pixel(0, 2, pozadina)

# Definirati sliku ovako točku po točku je nepraktično. Srećom postoji malo praktičniji način!

# Korak 1 -> definiramo varijable s bojama
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
W = (255, 255, 255)

slika = [
    G, G, G, G, G, G, G, G,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    G, G, G, G, G, G, G, G]

sense.clear()
sense.set_pixels(slika)

# Rotiranje slike
# Sliku možemo rotirati pomoći naredbe set_rotation(), kao parametar dajemo kut
# kut može imati vrijednosti od 0, 90, 180, 270
sense.set_rotation(90)

kutevi = [0, 90, 180, 270, 0, 90, 180, 270]

for kut in kutevi:
    sense.set_rotation(kut)
    time.sleep(0.5)

# Postoje i funkcije za zrcaljenje po horizontalnoj ili vertikalnoj osi
# flip_h() i flip_v()











