### OSNOVNI KORACI ###
### PISANJE - DUMP ###

# 0. Preduvjet
import json 

# 1. Podaci/objekt koji želimo pohraniti u datoteku - rječnik
user = {
    "id": 1,
    "first_name": "Petar",
    "last_name": "Perić",
    "user_name": "pperic",
    "email": "pperic@gmail.com",
    "address": {
        "street": "Ilica 200",
        "city": "Zagreb",
        "zip_code": 10000
    }
}

# 2. Zapisivanje u datoteku 
# try:
#     with open('user.json', 'w') as file_writer:
#         # koristimo json.dump()
#         # 1. argument je što zapisujemo
#         # 2. opcionalan, stream za pisanje u datoteku
#         json.dump(user, file_writer)

# except Exception as e:
#     print(e)

try:
    with open('user.json', 'w') as file_writer:
        # koristimo json.dump()
        # 1. argument je što zapisujemo
        # 2. opcionalan, stream za pisanje u datoteku
        json.dump(user, file_writer, indent = 4)

except Exception as e:
    print(e)

### OSNOVNI KORACI ###
### ČITANJE - LOAD(S) ###

# 0. Preduvjet
import json 

tekst_json = ''
try:
    with open('user.json', 'r') as file_reader:
        tekst_json = file_reader.read()

except Exception as e:
    print(e)

dict_json = json.loads(tekst_json)
print(dict_json['first_name'])

dict_json = {}
# Pokušat ćemo direktno iz datoteke procitati tekst i pretvoriti ga u dict objekt
try:
    with open('user.json', 'r') as file_reader:
        dict_json = json.load(file_reader)
except Exception as e:
    print(e)
