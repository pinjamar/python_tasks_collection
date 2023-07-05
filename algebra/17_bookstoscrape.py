import requests
from bs4 import BeautifulSoup

sirovi_podaci = requests.get("http://books.toscrape.com/").content

opis_ocjena = {
    "One": "*",
    "Two": "**",
    "Three": "***",
    "Four": "****",
    "Five": "*****"
}

def get_ocjena(tag):
    for naziv, broj_zvjezdica in opis_ocjena.items():
        if naziv in tag["class"]:
            return broj_zvjezdica
        
# Pretvaramo sirove podatke u čitljivi skup HTML tagova
sadrzaj = BeautifulSoup(sirovi_podaci, 'html.parser')

cijene = sadrzaj.select(".price_color")
naslovi = sadrzaj.select(".product_pod h3 a")
ocjene = sadrzaj.select(".star-rating")

# Moramo proći kroz gore kreirane liste i njihov sadržaj ćemo pohraniti u tekstualnu datoteku
# koristit ćemo .csv file (slično kao i .txt i vrijede ista pravila), zgodno je jer se može otvarati u excelu
# print(cijene[0])
with open("books.txt", "w", encoding="utf-8") as file_writer:
    for cijena, naslov, ocjena in zip(cijene, naslovi, ocjene):
        # zip() je funkcija koja kao parametar prima više kolekcija, zatim iz svake vraća po jedan element 
        # u prethodno definirane varijable
        file_writer.write(f"{naslov['title']};{cijena.text};{get_ocjena(ocjena)}\n")