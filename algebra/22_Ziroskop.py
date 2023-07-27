# Na Sense HAT simulatoru imate dio naziva Orientation
# Tu imate vrijednosti kuteva zakreta oko x, y i z osi
    # x = Roll
    # y = Pitch
    # z = Yaw
    
# Kao i uvijek, isto pravilo za početak programa!
from sense_emu import SenseHat
sense = SenseHat()

# ziroskop = sense.get_orientation()
# print(ziroskop)

# Dobijemo rječnik s vrijednostima -> imamo {} zagrade i key - value parove

# roll, pitch, yaw = ziroskop.values()

roll, pitch, yaw = sense.get_orientation().values()

roll = round(roll, 2)
pitch = round(pitch, 2)
yaw = round(yaw, 2)

mjerenje = f'Roll: {roll}; Pitch {pitch}; Yaw: {yaw}'
# sense.show_message(mjerenje)

# Drugi način orijentacije je pomoću akcelerometra i funkcije get_accelerometer_raw
accelerometer = sense.get_accelerometer_raw().values()
print(accelerometer)

# Možemo primijetiti da su dobivene vrijednosti između -1 i 1
# Senzor nam mjeri 'g' ubrzanje u smjeru osi x, y, z
