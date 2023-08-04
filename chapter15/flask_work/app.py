from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html/hello.html') # html/index.htmlを表示しますよという指定

@app.route('/flask') #/flaskというpath
def flask_hello():
    return render_template('html/flask.html') # html/flask.htmlファイルに飛ばす

# @app.route('/python')
# def hello_python():
#     return 'Hello Python world!'

if __name__ == '__main__':
    app.run(debug=True)
