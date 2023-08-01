from FileManager import *
from JsonManager import *

users_dict = read_from_json_convert_to_dict('users.json')

print(type(users_dict))

# Sad npr. želimo iz našeg dict_json uzeti id, name i email od svakog usera i pohraniti to u neku tekstualnu datoteku
# VAŽNO! -> obratite pažnju na tip varijable users_dict

for user in users_dict:
    
    ime = user['name']
    email = user['email']

    append_to_file_path_open_close('users.txt', f'{ime}\t({email})\n')
    


