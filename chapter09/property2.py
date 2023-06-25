class Property:
    def __init__(self):
        self.__x = 100
        self.__y = 200
        self.__z = 18

    @property # x と yに対して変数名で関数を作る & 値を読み込むことができる
    def x(self):
        return self.__x

    @x.setter # x と yに対して変数名で関数を作る & 値を読み込むことができる
    def x(self, x):
        self.__x = x
    
    
    @property
    def y(self):
        return self.__y
    
    @y.setter # x と yに対して変数名で関数を作る & 値を読み込むことができる
    def y(self, y):
        self.__y = y
    
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, z):
        self.__z = z
    
proper = Property()
# print(proper.__x) # __をつけているのはprivate関数なのでクラスの外のインスタンス化したものでは干渉できない
# print(proper.__y)
print(proper.x)  # private関数に干渉できるようにするためのgetter
print(proper.y)
# propertyを使うことで簡潔に書くことができる
# proper.x = 3000000000000 #値の更新、エラーになる
proper.y = 90900909
proper.z = 3
print(proper.y)
print(proper.z)
# 弾いたりできる　for example チートでジェムの数を10000にしようとしてもsetterでジェムは10000以上にできないという条件を作って弾くことができる
