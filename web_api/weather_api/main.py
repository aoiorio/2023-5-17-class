import requests


def search_weather():
    # APIの取得
    url = f"https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
    response = requests.get(url)
    # 辞書型になっている値をjsonでレスポンス形式にしてdataに代入する
    data = response.json()
    print(data['latitude'])


def search_rain():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,precipitation&forecast_days=1"
    response = requests.get(url)
    data = response.json()
    print(data)

# 関数を実行する
search_weather()
search_rain()