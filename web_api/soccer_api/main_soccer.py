import requests


def soccer_api():
    url = f"https://api.football-data.org/v4/matches"
    headers = {
        'X-Auth-token': 'API KEY'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    for match in data['matches']:

        print(match)


soccer_api()
# My API key API KEY