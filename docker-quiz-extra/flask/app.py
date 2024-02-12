from flask import Flask

app = Flask(__name__)

# Hello world!!を返す
@app.route('/')
def index():
    return "Hello world!!"

# portを設定する
if __name__ == '__main__':
    # appを起動させるpathの指定
    app.run(host='0.0.0.0', port=3030)