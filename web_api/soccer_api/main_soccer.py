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

# print("-----------------------------------------------")

# import http.client
# import json

# connection = http.client.HTTPConnection('api.football-data.org')
# headers = { 'X-Auth-Token': '872b5ca0a4f64cf281154f6f53d38962' }
# connection.request('GET', '/v2/competitions/DED', None, headers )
# response = json.loads(connection.getresponse().read().decode())

# print (response)