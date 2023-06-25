class Fibs:
    def __init__(self): # 初期化
        self.a = 0
        self.b = 1
    def __next__(self):
        # 前の２項を足したものをself.bに準備
        self.a, self.b = self.b, self.a+self.b
        return self.a # self.a を返す
    def __iter__(self):
        return self
    
fibs = Fibs()
print(fibs)

for f in fibs:
    print(f)
    if f > 1000:
        print(f)
        break