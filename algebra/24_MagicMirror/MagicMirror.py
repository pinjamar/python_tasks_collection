import requests
import datetime as dt
from bs4 import BeautifulSoup


def daily_quote():
    url = f"http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
    response = requests.get(url)
    data = response.json()
    quote = data['thought']['quote']
    return quote

def date():
    date = dt.datetime.now()
    return f"{date:%A, %B %d, %Y}"


def temperature_st():
    url = f'https://freemeteo.com.hr/vrijeme/split/trenutno-vrijeme/mjesto/?gid=3190261&language=croatian&country=croatia'
    response = requests.get(url).content
    temp_meteo = BeautifulSoup(response, 'html.parser')
    data_of_temperature = temp_meteo.find('div', class_='temp')
    # print(message)
    return f'☀ {data_of_temperature.text}' #pretvaranje u tekst
    #Uljepšati

# resp = requests.get(URL).content

# covid_stranica = BeautifulSoup(resp, 'html.parser')

# svi_podaci = covid_stranica.find_all('div', id = "maincounter-wrap")
# print(svi_podaci) 


