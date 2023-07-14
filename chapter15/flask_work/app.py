from flask import Flask

app = Flask(__name__)

@app.route('/')
def powers(n=10):
    return ' next'.join(str(2**i) for i in range(n))

@app.route('/hello')
def hello():
    return f'hello atom'

@app.route('/python')
def hello_python():
    return 'Hello Python world!'

if __name__ == '__main__':
    app.run(debug=True)