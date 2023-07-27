# Na Sense HAT Emulatoru imamo dio koji se naziva Joystick
# Ovaj dio emulatora nam prati događaje ili evente koji se dogode svaki put kad korisnik:
    # pomakne palicu u nekom smjeru (lijevo, desno, gore, dolje)
    # pusti palicu (možemo pratiti je li korisnik pomaknuo PALICU i DRŽI je id alje u tom smjeru
      # ili je pustio palicu
    # kada korisnik pritisne palicu
    
# Svaki događaj / event ima nekoliko podataka koje možemo koristiti. Podaci uz svaki event su:
    # timestamp - vrijeme događaja
    # direction - smjer pomicanja palice, a vrijednosti su up, down, left, right, middle (za pritisak palice)
    # action - pressed i released
    
from sense_emu import SenseHat
import time

sense = SenseHat()

# Za pristup komandnoj palici koristimo sense.stick svojstvo SenseHat objekta
# dogadaji = sense.stick.get_events()
# print(dogadaji)

# Gornji print nam je vratio prazno polje zato što se nije dogodio niti jedan događaj
# Zato trebamo kontinuirano pratiti ili "slusati" hoce li se dogoditi neki event!

# while True:
#     events = sense.stick.get_events()
#     print(events)
    
# Očitanja se događaju jako brzo pa u konzoli ne možemo pratiti što se događa
# Možemo pauzirati izvršavanje programa na jednu sekundu

# while True:
#     events = sense.stick.get_events()
#     print(events)
#     time.sleep(1)

# Provjerimo kako izgledaju podaci koje dobijemo uz svaki event
# while True:
#     for event in sense.stick.get_events():
#         print(event.direction, event.action)
        
# Probajmo još malo više uljepšati ispis
# Ako palica miruje ispisati palica miruje
# Ako je palica pritisnuta - ispisati da je pritisnuta i dodati smjer
# Ako je palica otpustena - ispisati da je otpuštena i dodati smjer iz kojeg je vraćena u mirovanje
# To ponavljati u beskonačnost

# while True:
#     events = sense.stick.get_events()
#     if events:
#         for event in events:
#             if event.action == 'pressed':
#                 print('Palica je pomaknuta', end = ' ')
#                 if event.direction == 'up':
#                     print('prema gore')
#                 elif event.direction == 'down':
#                     print('prema dolje')
#                 elif event.direction == 'left':
#                     print('prema lijevo')
#                 elif event.direction == 'right':
#                     print('prema desno')
#                 elif event.direction == 'middle':
#                     print(', NIJE pomaknuta pritisnuta je')
#             elif event.action == 'released':
#                 print('Palica je otpustena', end = ' ')
#                 if event.direction == 'up':
#                     print('prema gore')
#                 elif event.direction == 'down':
#                     print('prema dolje')
#                 elif event.direction == 'left':
#                     print('prema lijevo')
#                 elif event.direction == 'right':
#                     print('prema desno')
#                 elif event.direction == 'middle':
#                     print(', NIJE otpuštena je')
#     else:
#         print('Palica miruje')
#     
#     time.sleep(1)
#     sense.clear()

# Možemo iskoristiti LED ekran i ispisati početno slovo ovisno o smjeru u kojem smo pomaknuli
# palicu

# while True:
#     for event in sense.stick.get_events():
#         if event.action == 'pressed':
#             if event.direction == 'up':
#                 sense.show_letter("U")
#             elif event.direction == 'down':
#                 sense.show_letter("D")
#             elif event.direction == 'left':
#                 sense.show_letter("L")
#             elif event.direction == 'right':
#                 sense.show_letter("R")
#             elif event.direction == 'middle':
#                 sense.show_letter("M")
#             time.sleep(1)
#             sense.clear()

# ZADATAK
# p = (0, 0, 255)
# s = (0, 102, 102)
# b = (255, 255, 255)
# z = (204, 204, 0)
# pr = (0, 0, 0)
# 
# ljubimac = [
#     pr, pr, pr, pr, pr, pr, pr, pr,
#     p, pr, pr, pr, pr, pr, pr, pr,
#     pr, p, pr, pr, p, pr, p, pr,
#     pr, p, s, s, p, b, b, pr,
#     pr, s, s, s, b, z, b, z,
#     pr, s, s, s, s, b, b, pr,
#     pr, s, pr, s, pr, s, pr, pr,
#     pr, pr, pr, pr, pr, pr, pr, pr]
# 
# ljubimac2 = [
#     pr, pr, pr, pr, pr, pr, pr, pr,
#     p, pr, pr, pr, pr, pr, pr, pr,
#     pr, p, pr, pr, p, pr, p, pr,
#     pr, p, s, s, p, b, b, pr,
#     pr, s, s, s, b, z, b, z,
#     pr, s, s, s, s, b, b, pr,
#     pr, pr, s, pr, s, pr, pr, pr,
#     pr, pr, pr, pr, pr, pr, pr, pr]
# 
# sense.clear()
# # sense.set_pixels(ljubimac)
# 
# def setnja():
#     for i in range(10):
#         sense.set_pixels(ljubimac)
#         time.sleep(0.5)
#         sense.set_pixels(ljubimac2)
#         time.sleep(0.5)
# 
# while True:
#     events = sense.stick.get_events()
#     if events:
#         if events[0].direction == 'right':
#             setnja()

#######

def crveno():
    sense.clear(255, 0, 0)
    
def plavo():
    sense.clear(0, 0, 255)
    
def zeleno():
    sense.clear(0, 255, 0)
    
def zuto():
    sense.clear(255, 255, 0)
    
sense.stick.direction_up = crveno
sense.stick.direction_down = plavo
sense.stick.direction_left = zeleno
sense.stick.direction_right = zuto
sense.stick.direction_middle = sense.clear

while True:
    pass

# ZADATAK
# Napravite aplikaciju koja će u txt datoteku pohraniti sve meteo ili joystick događaje i očitanja

# Zapisujete u txt u obliku VRIJEME_OCITANJA; SENZOR (naziv velicine/dogadaja); OCITANA VRIJEDNOST

# DODATNO:
# 1. Pohranite u json formatu
# 2. Pohranitu u SQLite bazu
    