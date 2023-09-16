import requests


def soccer_api():
    url = f"https://api.football-data.org/v4/matches"
    headers = {
        'X-Auth-token': '872b5ca0a4f64cf281154f6f53d38962'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    for match in data['matches']:

        print(match)


soccer_api()
# 872b5ca0a4f64cf281154f6f53d38962