import sqlite3 # 

#データベースに接続
conn = sqlite3.connect('text.db')
# データベースのカーソルを取得
cursor = conn.cursor()

# テーブルを作成 executeは実行という意味
cursor.execute('''
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
);
''')

query ='INSERT INTO test (name, email) VALUES (?, ?)'
cursor.execute(query, ('Yamada Taro', 'taro@email.com')) # ?, ? に入れたい値を入れることができる
cursor.execute(query, ('Yamada Taro', 'taro@email.com')) # ?, ? に入れたい値を入れることができる
cursor.execute(query, ('Yamada Taro', 'taro@email.com')) # ?, ? に入れたい値を入れることができる
cursor.execute(query, ('Yamada Taro', 'taro@email.com')) # ?, ? に入れたい値を入れることができる

conn.commit()
conn.close()
