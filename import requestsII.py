import requests

base_url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {"q": "Rocklin,CA", "appid": "4504a5729590b5a17743f43c25d971c0"}

response = requests.get(base_url, params = parameters)

print(response.text)