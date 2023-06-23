class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    # def set_size(self, size):
    #     self.width,self.height = size
    # def get_size(self):
    #     return self.width,self.height
    @property
    def size(self):
        return self.__width, self.__height
    @size.setter
    def size(self, size):
        self.__width, self.__height = size
    # size = property(get_size, set_size)  # 追加

r = Rectangle(101, 3) # インスタンス化
# r.width = 10 # widthの値を設定
# r.height = 5 # heightの値を設定
print(r.size)          # 追加
print(r.size) # インスタンス化したrの値たちを取得する
r.size = 150, 44 # 変更
print(r.size)