import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS goods (
        goods_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        goods_name TEXT NOT NULL,
        goods_no INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''' )

query = 'INSERT INTO goods (goods_name, goods_no) VALUES (?, ?)'

cursor.execute(query, ('girl toy', 3))

conn.commit()
conn.close()