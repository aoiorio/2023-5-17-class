# import requests


# def soccer_api(self):
#     url = f"https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
#     response = requests.get(url)
#     data = response.json()
#     print(data)


# soccer_api(1)
# 872b5ca0a4f64cf281154f6f53d38962

import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '872b5ca0a4f64cf281154f6f53d38962' }
connection.request('GET', '/v2/competitions/DED', None, headers )
response = json.loads(connection.getresponse().read().decode())

print (response)