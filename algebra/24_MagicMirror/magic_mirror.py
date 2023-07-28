# 1. datum i vrijeme
# 2. vremenska prognoza
# 3. news portal (index najnovije vijesti) title i summary
# 4. cinestar popis filmova danas, naslov, (vrijeme?, slika?)
# 5. google kalendar i to do list

from news_scraper import *
from date_time import *
from weather_forecast import *
import tkinter as tk
from time import strftime

def vrime():
    dt = strftime('%H:%M:%S')
    lbl_time =tk.Label(root, text = dt)
    lbl_time.grid(row=0, column=0, padx =10, pady =10) 
    lbl_time.config(text=dt)
    lbl_time.after(100, vrime)

root = tk.Tk()

root.title("Magic Mirror")
root.geometry("600x400")

vrime()

url = "https://www.index.hr/najnovije?kategorija=3"

page = getPage(url)

news = getAllNews(page)

news_list = getNewsList(news)

news_list = news_list[:5]

for (i, news) in zip(range(5), news_list):
    lbl_title = tk.Label(root, text = news_list[i]["title"]).grid(row=i, column=1, padx =10, pady =10)
    lbl_summary= tk.Label(root, text = news_list[i]["summary"]).grid(row=i, column=2, padx =10, pady =10) 

key = "e4fcf4856c6957079ca70b9626dc1bc1"
city = "Zagreb"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}" 

weather_data = get_weather_forecast(url)

lbl_temp = tk.Label(root, text = weather_data["main"]["temp"]).grid(row=1, column=0, padx =10, pady =10) 
lbl_pressure = tk.Label(root, text = weather_data["main"]["pressure"]).grid(row=2, column=0, padx =10, pady =10) 
print(weather_data)
root.mainloop()
