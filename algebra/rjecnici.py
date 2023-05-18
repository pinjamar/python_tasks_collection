stanovnistvo = {
    "123456789": "Petar Peric",
    "274942048": "Marko Maric",
    "219430483": "Ivan Ivic",
    "846826319": "Josip Josipovic"
}

element = stanovnistvo["123456789"]

print(element)

for kljuc in stanovnistvo.keys():
    print(kljuc, end=" ")
print()

for value in stanovnistvo.values():
    print(value, end=" ")
print()

for key, value in stanovnistvo.items():
    print(key, value, end=";  ")
print()
