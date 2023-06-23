class Property:
    def __init__(self):
        self.__x = 100
        self.__y = 200

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
# 弾いたりできる　for example チートでジェムの数を10000にしようとしてもsetter 
proper = Property()
# print(proper.__x) # __をつけているのはprivate関数なのでクラスの外のインスタンス化したものでは干渉できない
# print(proper.__y)
print(proper.get_x())  # private関数に干渉できるようにするためのgetter
print(proper.get_y())
# propertyを使うことで簡潔に書くことができる