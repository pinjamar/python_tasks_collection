# ZADATAK: Kreirajte funkciju koja prima listu brojeva i vraća rječnik s dva ključa (count_even, count_odd) 
# čije vrijednosti su broj ponavljanja parnih i neparnih brojeva u listi. 

# PRIMJER: [1,2,3,4,5,6,7] -> dict { count_even: 3, count_odd: 4}

def count_even_odd(numbers):
    count_even = 0
    count_odd = 0

    for num in numbers:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    result = {
        'count_even': count_even,
        'count_odd': count_odd
    }
    return result