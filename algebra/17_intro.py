import urllib.request
from bs4 import BeautifulSoup

URL = 'https://www.algebra.hr'
konekcija = urllib.request.urlopen(URL)
sadrzaj = konekcija.read().decode()
print(type(sadrzaj))

podaci = BeautifulSoup(sadrzaj, 'html.parser')
print(dir(podaci))
paragrafi = podaci.find_all('p')
print(type(paragrafi))
for paragraf in paragrafi:
   print(paragraf.text)
