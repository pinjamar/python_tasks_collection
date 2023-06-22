# ZADATAK: Kreirajte funkciju koja prima listu brojeva, a vraća listu čiji elementi su kvadrat elemenata iz ulazne liste

# Pri rješavanju koristite WHILE petlju.

def square_machine(poc_lista):
    i = 0
    while i < len(poc_lista):
        poc_lista[i] = poc_lista[i]**2
        i += 1
    return poc_lista


# print(square_machine([1,2,3,4,5,6]))

input_string = input('Unesite elemente liste odvojene razmakom!')
user_list = input_string.split()

print('lista je', user_list)