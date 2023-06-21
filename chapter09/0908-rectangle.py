class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    
    def set_size(self, size):
        self.width,self.height = size
    def get_size(self):
        return self.width,self.height
    size = property(get_size, set_size)  # 追加

r = Rectangle() # インスタンス化
r.width = 10 # widthの値を設定
r.height = 5 # heightの値を設定
print(r.size)          # 追加
print(r.get_size()) # インスタンス化したrの値たちを取得する
r.size = 150, 44 # 変更
print(r.width)
print(r.height)