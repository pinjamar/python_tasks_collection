"""
Reflector: B
Rotors I - II - III
Plugboard: A-R, G-K, O-X
Message: A=>X
"""
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from keyboard import Keyboard
from enigma import Enigma

# Historical engima components - rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E')
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V')
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", 'J')
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", 'Z')

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

KB = Keyboard()
PB = Plugboard(["AR", "GK", "OX"])

ENIGMA = Enigma(B, I, II, III, PB, KB)

# print(ENIGMA.encipher("A"))
# Sad ćemo vidjeti dobijemo li stvarno za slovo A -> X
# Set rings
ENIGMA.set_rings((1, 1, 1))

# Set message key
ENIGMA.set_key("DOG")

# ENIGMA.r3.show()

message = "TEST"
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)
print(cipher_text)

"""
letter = "A"
signal = KB.forward(letter)
signal = PB.forward(signal)
signal = III.forward(signal)
signal = II.forward(signal)
signal = I.forward(signal)
signal = A.reflect(signal)
signal = I.backward(signal)
signal = II.backward(signal)
signal = III.backward(signal)
signal = PB.backward(signal)
letter = KB.backward(signal)

print(letter)
"""

# I.show()
# I.rotate_to_letter("G")
# I.show()


