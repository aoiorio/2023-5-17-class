from flask import Flask, render_template, request
app = Flask(__name__) # インスタンスを作っていく

@app.route('/') # パスに対する振る舞いを書いていく
def index():
    tasks = {
        'title': 'task1',
        'detail': 'bread crusts',
        'due': '2023-07-19',
    }
    return render_template('index.html', tasks=tasks)

@app.route('/input', methods=['POST'])
def view_title():
    title = request.form['title']
    if title == '':
        title = 'No title'
    return render_template('input.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)