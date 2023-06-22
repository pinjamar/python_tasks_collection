# ZADATAK: Kreirajte funkciju is_prime koja kao parametar prima broj i vraća boolean ovisno o tome ako je broj
# prosti ili nije

# Prosti brojevi su brojevi koji su djeljivi samo s 1 i sa samim sobom
# NPR. 5 -> djeljiv samo s 5 i s 1
# NPR. 6 -> nije prosti jer je djeljiv i s 2 i s 3

# Prosti brojevi: 2, 3, 5, 7, 11, 13, 17, 19...

# LOGIKA: Dobijemo neki broj i onda ga pokušamo podijeliti redom sa svim brojevima koji su manji od njega, a
# veći od 1 -> ako pronađemo broj s kojim možemo podijeliti naš broj koji ispitujemo, onda on nije prosti !

# NPR. Imamo broj 5 -> probamo podijeliti s 4 -> 5 % 4 != 0 nije djeljiv s 4
                                        # s 3 -> 5 % 3 != 0 nije djeljiv s 3
                                        # s 2 -> 5 % 2 != 0 nije djeljiv s 2 -> ZAKLJUČAK: Broj je prost!

# HINT: 0, 1 nisu prosti !

# def is_prime(broj):
#     if broj < 2:
#         return False
#     else:
#         for num in range(2, broj):
#             if broj % num == 0:
#                 return False
#         return True
    
# Uzmimo za primjer 6 -> 1. iteracija if dio broj % num (6 % 2 == 0) dođemo do return dijela, vratimo False i završava se izvršavanje funkcije

# def is_prime(broj):
#     for i in range(2,broj):
#         if broj % i == 0:
#             return print(f'Broj {broj} nije prost.')
    
#     print(f'Broj {broj} je prost')

# a=int(input('Unesi jedan broj:'))
# print(is_prime(a))

# def is_prime(broj):
#     for i in range(2,broj):
#         if broj % i == 0:
#             return f'Broj {broj} nije prost.'
#     print(f'Broj {broj} je prost')


# a=int(input('Unesi jedan broj:'))
# print(is_prime(a))

# print(funkcija) -> uvijek isprinta ono što je sadržano u returnu.  
import random

# 1. mogućnost - return random.randint(0, 100)
# 2. mogućnost - return varijabla
# 3. mogućnost - print(random_number)

def random_int_generator():
    return random.randint(0, 100)

sluc_broj = random_int_generator()
print(sluc_broj)

print(random_int_generator())

def random_int_generator():
    slucajni_broj = random.randint(0, 100)
    return slucajni_broj

sluc_broj = random_int_generator()
print(sluc_broj)

print(random_int_generator())

def random_int_generator():
    print(random.randint(0, 100))

sluc_broj = random_int_generator()
print(sluc_broj)

random_int_generator()