import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        emp_name TEXT NOT NULL,
        emp_no INTEGER,
        department TEXT NOT NULL
);
''' )

query = 'INSERT INTO employee (emp_name, emp_no, department) VALUES (?, ?, ?)'

cursor.execute(query, ('horse toy', 1, 'ABCD mart'))
cursor.execute(query, ('manbo toy', 2, 'first store'))

conn.commit()
conn.close()