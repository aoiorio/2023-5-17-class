import requests
from flask import Flask, request, render_template

app = Flask(__name__)


def post_search(post_code):
    url = f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={post_code}'
    response = requests.get(url)
    data = response.json()

    return data['results'][0]


@app.route("/", methods=['GET', 'POST'])
def home():
    results = {}
    if request.method == 'POST':
        post_code = request.form.get('post_code')
        results = post_search(post_code)
        print(results)

    return render_template('search_post.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

# get weather information from open metro API
def search_weather(self):
    url = f'https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m'
    response = requests.get(url)
    data = response.json()
    print(data)

    return data['results'][0]

# if the url is /weather, users can see this page
@app.route("/weather", methods=['GET', 'POST'])
def home():
    weather_results = {}
    if request.method == 'POST':
        weather = request.form.get('post_code')
        weather_results = search_weather(weather)
        print(weather_results)

    return render_template('search_weather.html', weather_results=weather_results)