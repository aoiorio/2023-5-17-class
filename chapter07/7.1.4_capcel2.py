class Sample:
    # name = "orio" # 設定している部分が属性という
    __name = "aoi" # プライベート変数(クラス内でのみアクセス可能)
    __password = "password"  # プライベート変数(クラス内でのみアクセス可能)
    def hello(self):
        return "Hello! I'm " + self.__name + "!"
    def printhello(self):
        print(self.hello())
    
    def getName(self):
        return self.__name

a = Sample()
print(a.getName())
print(a.hello())
a.printhello()