import requests
from bs4 import BeautifulSoup

URL = 'https://www.worldometers.info/coronavirus/'

resp = requests.get(URL).content

covid_stranica = BeautifulSoup(resp, 'html.parser')

svi_podaci = covid_stranica.find_all('div', id = "maincounter-wrap")
print(svi_podaci)

# coronavirus_cases = svi_podaci[0]
# print(type(coronavirus_cases))

# print(svi_podaci[0])

# naslov = coronavirus_cases.find('h1').text
# vrijednost = coronavirus_cases.find('span').get_text()
# print(naslov)
# print(vrijednost)

for element in svi_podaci:
    naslov = element.find('h1').text
    vrijednost = element.find('span').text
    print(f'{naslov} {vrijednost}')
