import requests

def get_weather_forecast(url):

    response = requests.get(url)

    return response.json()