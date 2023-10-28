from flask import Flask

app = Flask(__name__)

# 下の文章でrouteを指定してURLに反映する
@app.route('/')
def index():
    return "Hello world!!"

# portを指定する（下記のコードでは3000番）
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
