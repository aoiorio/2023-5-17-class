import requests


def search_weather(self):
    # APIの取得
    url = f"https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
    response = requests.get(url)
    # 辞書型になっている値をjsonで取得してdataに代入する
    data = response.json()
    print(data)


search_weather(1)
