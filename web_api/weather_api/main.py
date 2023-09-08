import requests


def search_weather(self):
    url = f"https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    print(data)


search_weather(1)
