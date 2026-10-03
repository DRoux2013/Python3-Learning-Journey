import os
import requests

base_url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OPENWEATHER_API_KEY")

parameters = {"q": "Rocklin,CA", "appid": api_key}

response = requests.get(base_url, params=parameters)
print(response.text)