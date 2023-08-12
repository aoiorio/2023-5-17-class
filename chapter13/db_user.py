import sqlite3

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
# if not exists userはuserというテーブルがなかった時に新しく作るという条件を指定している
# NOT NULL はあってもなくてもいい
query ='INSERT INTO user (name, password, address, age) VALUES (?, ?, ?, ?)' # ??は後で入れるよという意味
cursor.execute(query, ('Aoi Orio', 'pass101', 'okinawa', 15)) # ?, ? に入れたい値を入れることができる
cursor.execute(query, ('Uemura', 'houhou1', 'tokyo', 26))
cursor.execute(query, ('DAreka', 'muo', 'hawaii', 89))
cursor.execute(query, ('hai', 'wai', 'america', 35))

conn.commit() # 追加した内容を確約する
conn.close() # databaseを
