# ZADATAK: Napravite aplikaciju koja će dohvatiti:
        # Sve podatke o korisnicima
        # Samo o jednom korisniku
        # Provjeriti ima li korisnika koji rade u istoj firmi, a ako ima koji su to korisnici
        # Za svakog od gore navedenog korisnika dohvatiti i prikazati postove koje su objavili
        # Generirati novu json datoteku sa svim zapisima za svakog korisnika

import requests
import json 

URL_USERS = 'https://jsonplaceholder.typicode.com/users'
URL_POSTS = 'https://jsonplaceholder.typicode.com/posts'

def get_response_and_convert_to_dict(url):
    response = requests.get(url).text
    return json.loads(response)

dict_users = get_response_and_convert_to_dict(URL_USERS)
dict_posts = get_response_and_convert_to_dict(URL_POSTS)

# novi_dict_users 1: [ime, prezime, adresa]


