from bs4 import BeautifulSoup
import requests
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.title("Kripto Market")

def get_page(url):
    try:
        resp = requests.get(url).content
    except requests.RequestException as e:
        print(e)
    return BeautifulSoup(resp, "html.parser")

def set_colour(x):
    if x >= 0:
        return '#008000'
    else:
        return '#ff0000'


def get_data_list(html_tag, html_class):
    return page.find_all(html_tag, html_class)

url = "https://coinmarketcap.com/"

page = get_page(url)

cripto_names = get_data_list("p", {"class" : "sc-4984dd93-0 kKpPOn"})[:5]

cripto_values = get_data_list("div", {"class" : "sc-bc83b59-0 iVdfNf"})[:5]

cripto_change_all = get_data_list("span", {"class" : "sc-97d6d2ca-0"})[:15]

cripto_change_values = []

for value in cripto_change_all:
    direction = value.find("span", {"class" : "icon-Caret-down"})
    val = value.text
    val = float(val[:-1])
    if direction:
        val *= -1
    cripto_change_values.append(val)

cripto_1h = cripto_change_values[::3]
cripto_24h = cripto_change_values[1::3]
cripto_7d = cripto_change_values[2::3]

for (i, name, value, x, y, z) in zip(range(5), cripto_names, cripto_values, cripto_1h, cripto_24h, cripto_7d):
    lbl_name = tk.Label(root, text = name.text, font = ("Arial", 16)).grid(row = i, column = 0, sticky="w")
    lbl_value = tk.Label(root, text = value.find("span").text, font = ("Arial", 16)).grid(row = i, column = 1, sticky="e")
    
    lbl_1h = tk.Label(root, text = x, font = ("Arial", 16), fg=set_colour(x)).grid(row = i, column = 2)
    lbl_24h = tk.Label(root, text = y, font = ("Arial", 16), fg=set_colour(y)).grid(row = i, column = 3)
    lbl_7d = tk.Label(root, text = z, font = ("Arial", 16), fg=set_colour(z)).grid(row = i, column = 4)

root.mainloop()