### ČITANJE - READ - 'r' ###
### Adresar - pokušaj 1 ###
# Koristit ćemo adresar.txt za čitanje

# try:
#     with open('data/adresar.txt', 'r') as file_reader:
#         file_data = file_reader.read()
#         print(file_data)

# except Exception as e:
#     print(f'Dogodila se greška {e}')

### Adresar - pokusaj 2 ###
# Ajmo pokušati čitati redak po redak 
# try:
#     with open('data/adresar.txt', 'r') as file_reader:
#         for red in file_reader:
#             dijelovi_retka = red.split(';')
#             print(f'ID: {dijelovi_retka[0]}\tIme: {dijelovi_retka[1]}\tPrezime: {dijelovi_retka[2]}\tTelefon: {dijelovi_retka[3]}')

# except Exception as e:
#     print(e)

### ADRESAR - Pokušaj 3 ###

class Contact:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def print_contact(self):
        print(f'Name: {self.first_name}\tSurname: {self.last_name}\tPhone: {self.phone}')

# objekt1 = Contact(1, 'filip', 'skendrovic', '098328393482')
# print(objekt1)

address_book = {}

try:
    with open('data/adresar.txt', 'r') as file_reader:
        for line in file_reader:
            line_parts = line.split(';') # line_parts je lista s elementima: id, first, last, phone
            contact = Contact(line_parts[0], line_parts[1], line_parts[2], line_parts[3])
            address_book[contact.id] = contact

except Exception:
    print(Exception)

for key, value in address_book.items():
    print(key, end = '\t')
    value.print_contact()

# contact1 = Contact('a', 'a', 'a', 'a')
# contact2 = Contact('b', 'b', 'b', 'b')
# contact3 = Contact('c', 'c', 'c', 'c')

# contact1.print_contact()

# contact2.print_contact()