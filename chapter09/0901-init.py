class FooBar:
    def __init__(self, value=15):# initは一番最初に勝手に設定してくれる　15を初期値として設定
        self.somevar = value

f = FooBar("これはコンストラクタの引数です") # インスタンス化する　括弧内に引数をセットする
print(f.somevar) # print文でsomevarに設定された値を出力する　
g = FooBar() # 何も渡さないと15という値になる初期設定してるから
print(g.somevar)