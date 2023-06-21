class A:
    def hello(self):
        print("Hello I'm A.")

class B(A): # Bでオリジナルの処理をしたい！！
    def hello(self):
        print("Hello I'm B.") # AをBにする
    
    def helloA(self):
        super().hello()

# インスタンス化
a = A()
b = B()

a.hello()
b.hello()
b.helloA()
