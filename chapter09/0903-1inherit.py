class A:
    def hello(self):
        print("Hello I'm A.")

class B(A): # Bでオリジナルの処理をしたい！！
    def hello(self):
        print("Hello I'm B.") # AをBにする(class Aの関数を上書きする)
    
    def helloA(self):
        super().hello() # class Aの関数helloを持ってきている

# インスタンス化
a = A()
b = B()

a.hello()
b.hello()
b.helloA()
