import requests
response = requests.get("data")
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    #pip install requests==2.34.2 might be needed to avoid update conflicts
    