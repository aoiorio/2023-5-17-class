from connection import *


class Goods:
    def __init__(self):
        self.connection = SQLiteConnection('test.db') #
        self.connection.connect()
    def goods_insert(self, goods_name, goods_no):
        query = 'INSERT INTO goods (goods_name, goods_no) VALUES (?, ?)'
        self.connection.execute_query(query, goods_name, goods_no)
        self.connection.close() # databaseを閉じる
