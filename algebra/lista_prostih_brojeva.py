# ZADATAK: Koristeći funkciju is_prime iz prethodnog zadatka napišite kod koji vraća proste brojeve u nekom definiranom rasponu. Početak i kraj
# raspona definira sam korisnik. NPR. korisnik unese poečtak raspona 4 i kraj 11, program mu ispiše 5, 7, 11. 

# Osim toga potrebno je ispisati koliki je broj prostih brojeva u tom intervalu. Naravno, iskoristite formatirane rečenice.
# Ako korisnik unese krajnji broj koji je manji od početnog, potrebno mu je napomenuti da je unesao pogrešan broj i omogućiti mu da isti 
# unese ponovno

def is_prime(broj):
    if broj < 2:
        return False
    else:
        for num in range(2, broj):
            if broj % num == 0:
                return False
        return True

start_range = int(input('Unesite početni broj u rasponu:\t'))
end_range = int(input('Unesit posljednji broj u rasponu:\t'))

while end_range < start_range:
    print('Krajnji broj ne smije biti manji od početnog. Pokušajte ponovno:')
    end_range = int(input('Unesit posljednji broj u rasponu:\t'))

# num_of_primes = 0
primes = []

for num in range(start_range, end_range + 1):
    if is_prime(num):
        # num_of_primes += 1
        primes.append(num)

print(f'Postoji {len(primes)} prostih brojeva u rasponu od {start_range} do {end_range}')
print(f'Prosti brojevi u traženom rasponu su: {primes}')

