class MyClass:
    age = 22
    @staticmethod
    def smeth(): # 引数selfなしで定義されます。クラス名を指定して直星つ呼び出せます
        print("This is a staticmethod.")
    @classmethod
    def cmeth(cls): # 引数selfの代わりにそのクラスの値を使う(cls)
        print(f"This is a {cls.age} class method.")

MyClass.smeth()
MyClass.cmeth()