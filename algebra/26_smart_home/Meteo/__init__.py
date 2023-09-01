import requests
from bs4 import BeautifulSoup


class grad:
    ime = ""
    temp = ""
    vlaga = ""
    tlak = ""

    def __init__(self, grad_xml):
        self.ime = grad_xml.find("GradIme").text
        self.temp = float(grad_xml.find("Temp").text)
        self.vlaga = grad_xml.find("Vlaga").text
        self.tlak = grad_xml.find("Tlak").text


def podaci():
    sirovi_podaci = requests.get('https://vrijeme.hr/hrvatska_n.xml').content
    sadrzaj = BeautifulSoup(sirovi_podaci, 'xml')
    gradovi = sadrzaj.find_all('Grad')
    pravi_gradovi = []
    for gr in gradovi:
        city = grad(gr)
        pravi_gradovi.append(city)
    return pravi_gradovi
