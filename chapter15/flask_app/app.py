from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) # インスタンスを作っていく
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db" #dbを作っている
db = SQLAlchemy(app) # SQLAlchemyのdbというインスタンスが作成できる

class Task(db.Model):
    __tablename__ = "Task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False) # 最大の文字数をdb.Stringの後ろに(文字数)をつけて設定できる
    detail = db.Column(db.String(20), nullable=False)
    due = db.Column(db.String(10), nullable=False)

class User(db.Model): # Userというデータベースを作って
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(30), nullable=False)

@app.route('/') # パスに対する振る舞いを書いていく
def index():
    tasks = Task.query.all()
    print(tasks)
    for task in tasks:
        print(task.title, task.detail)

    return render_template('index.html', tasks=tasks)

@app.route('/user_form')
def user_page():
    users = User.query.all()
    return render_template('user_form.html', users=users)

@app.route('/input', methods=['POST'])
def view_title():
    if request.method == 'POST':
        task = Task(
            title=request.form['task_name'],
            detail=request.form['detail'],
            due=request.form['due'])
        db.session.add(task) # dbにtaskの内容を追加
        db.session.commit() # 確約する
        return redirect('/') # /のページに(index.htmlに)飛ばすよということ

@app.route('/user_form/input', methods=['POST'])
def view_user():
    if request.method == 'POST':
        user = User(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/user_form')



if __name__ == '__main__':
    app.run(debug=True)
