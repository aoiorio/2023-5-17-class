import sqlite3 # sqlite3を追加

#データベースに接続
conn = sqlite3.connect('user.db')
# データベースのカーソルを取得
cursor = conn.cursor()

# テーブルを作成 executeは実行という意味
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        address TEXT NOT NULL,
        age INTEGER NOT NULL
);
''') 
# testというテーブルがなかったら新たに作るというコード
# sqlite3の書き方は全て英語の大文字です。　

query ='INSERT INTO user (name, password, address, age) VALUES (?, ?, ?, ?)' # ??は後で入れるよという意味
cursor.execute(query, ('Aoi Orio', 'pass101', 'okinawa', 15))# ?, ? に入れたい値を入れることができる


conn.commit()
conn.close()
