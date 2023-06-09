# ZADATAK: Kreirajte funkciju password_generator koja vraća n passworda određene duljine. 
# Za duljinu passworda i broj passworda koji želi generirati pitamo usera!
# Uvjet: lozinka (password) ne smije sadržavati manje od 5 znakova.
# Password može sadržavati upper i lowercase znakove engleskoh alfabeta i specijalne znakove '!@#$%'

import random

NUMERIC_CHARS = "0123456789"
LOWERCASE_CHARS = "abcdefghijklmnopqrstvwxyz"
UPPERCASE_CHARS = LOWERCASE_CHARS.upper()
SPECIAL_CHARS = '!@#$%'

pass_chars = NUMERIC_CHARS + LOWERCASE_CHARS + UPPERCASE_CHARS + SPECIAL_CHARS
# '0123456789abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ!@#$%'

def password_generator(password_length, number_of_passwords):
    passwords = []

    for n in range(num_of_pass):
        password = ""
        for c in range(pass_len): # korisnik će reći da želi password duljine 7
            # password += pass_chars[random.randint(0, len(pass_chars)-1)]
            password += random.choice(pass_chars)
        passwords.append(password)

    for password in passwords:
        print(password)

pass_len = int(input('Unesite koliko znakova mora sadržavati vaša lozinka\t'))
while pass_len < 5:
    print('Lozinka mora sadržavati 5 ili više znakova. Pokušajte ponovno:\t')
    pass_len = int(input('Unesite koliko znakova mora sadržavati vaša lozinka\t'))

num_of_pass = int(input('Unesite koliko passworda želite generirati:\t'))

password_generator(pass_len, num_of_pass)