class FooBar:
    def __init__(self, value):
        self.somevar = value
        print(f"init:{self.somevar}")

f = FooBar("これはコンストラクタの引数です")
