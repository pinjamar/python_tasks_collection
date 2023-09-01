import tkinter as tk
from Meteo import podaci, grad


def temperature_icon(temp):
    if (temp > 22):
        return f'☀️'
    elif (12 < temp <= 22):
        return '⛅'
    elif (0 < temp <= 12):
        return f'☁️'
    else:
        return f'❄️'


def weather_tab(notebook):
    gradovi = podaci()
    split = gradovi[33]

    meteo_tab = tk.Frame(notebook)
    notebook.add(meteo_tab, text='Meteo')

    temp_lbl = tk.Label(meteo_tab, text='Temperatura: ')
    temp_lbl.grid(row=0, column=0, padx=10, pady=5, sticky='w')

    temp_city_lbl_city = tk.Label(
        meteo_tab, text=f'- u gradu (Split-Marjan): {split.temp} °C - {temperature_icon(split.temp)}')
    temp_city_lbl_city.grid(row=1, column=0, padx=10, sticky='w')
    temp_city_lbl_home = tk.Label(
        meteo_tab, text=f'- u kući (Split-Marjan): {split.temp * 0.9} °C {temperature_icon(split.temp * 0.9)}')
    temp_city_lbl_home.grid(row=2, column=0, padx=10, sticky='w')

    humidity_lbl = tk.Label(meteo_tab, text='Vlažnost zraka: ')
    humidity_lbl.grid(row=3, column=0, padx=10, pady=5, sticky='w')

    humidity_city_lbl = tk.Label(
        meteo_tab, text=f'- u gradu (Split-Marjan): {split.vlaga} %')
    humidity_city_lbl.grid(row=4, column=0, padx=10, sticky='w')
    humidity_home_lbl = tk.Label(
        meteo_tab, text=f'- u kući (Split): {split.vlaga} %')
    humidity_home_lbl.grid(row=5, column=0, padx=10, sticky='w')

    air_pressure_lbl = tk.Label(meteo_tab, text='Tlak zraka: ')
    air_pressure_lbl.grid(row=6, column=0, padx=10, pady=5, sticky='w')

    air_pressure_city_lbl = tk.Label(
        meteo_tab, text=f'- u gradu (Split-Marjan): {split.tlak} hPa')
    air_pressure_city_lbl.grid(row=7, column=0, padx=10, sticky='w')
    air_pressure_home_lbl = tk.Label(
        meteo_tab, text=f'- u kući (Split): {split.tlak} hPa')
    air_pressure_home_lbl.grid(row=8, column=0, padx=10, sticky='w')
