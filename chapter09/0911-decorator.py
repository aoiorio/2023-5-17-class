class MyClass:
    age = 22
    @staticmethod
    def smeth(): # 引数selfなしで定義されます。クラス名を指定して直星つ呼び出せます
        print("This is a staticmethod.")
    @classmethod
    def cmeth(cls, age):
        cls.age += age # 引数selfの代わりにそのクラスの値を使う(cls) クラス専用の値に干渉する時に使う
        print(f"This is a {cls.age} class method.")

    def imeth(self, age):
        self.age += age
        print(f"This is a {self.age} instance method")


MyClass.smeth()
MyClass.cmeth(age=10)
ins = MyClass()
ins.imeth(age=2)
ins2 = MyClass() # 追加
ins2.imeth(age=10)