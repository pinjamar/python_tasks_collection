vozni_park = {
    1: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3: ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4: ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5: ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.00],
    6: ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7: ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8: ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00]
}

print()
print('Ispis PRIJE određene naredbe:')
for kljuc, vrijednost in vozni_park.items():
    print(kljuc, end = '\t')
    for element in vrijednost:
        print(element, end = '\t')
    print()
print()

### CLEAR ###
# vozni_park.clear()

# print('Ispis NAKON clear()')
# for key, value in vozni_park.items():
#     print(key, end = '\t')
#     for i in value:
#         print(i, end = '\t')
#     print()
# print()

### POP ###
# vrijednost_1 = vozni_park.pop(1, 'Ne postoji traženi element u bazi')

# print('Ispis NAKON pop(1):')
# for key, value in vozni_park.items():
#     print(key, end = '\t')
#     for i in value:
#         print(i, end = '\t')
#     print()
# print()
# print('Vraćena vrijednost pomoću pop(1):', vrijednost_1)
# print()

# vrijednost_10 = vozni_park.pop(10, 'Ne postoji traženi element u bazi!')

# print('Ispis NAKON pop(10)')
# for key, value in vozni_park.items():
#     print(key, end = '\t')
#     for i in value:
#         print(i, end = '\t')
#     print()
# print()
# print('Vraćena vrijednost pomoću pop(10)', vrijednost_10)
# print()

### POPITEM ###

# vrijednost_1 = vozni_park.popitem()
# print()
# print('Ispis NAKON popitem()')
# for key, value in vozni_park.items():
#     print(key, end = '\t')
#     for i in value:
#         print(i, end = '\t')
#     print()
# print()
# print('Vraćena vrijednost pomoću popitem()', vrijednost_1)
# print()

# vrijednost_2 = vozni_park.popitem()
# print('Ispis NAKON još jednog popitem():')
# for key, value in vozni_park.items():
#     print(key, end = '\t')
#     for i in value:
#         print(i, end = '\t')
#     print()
# print()
# print('Vraćena vrijednost pomoću popitem()', vrijednost_2)
# print()

print(vozni_park.values())
print()
print(vozni_park.keys())


