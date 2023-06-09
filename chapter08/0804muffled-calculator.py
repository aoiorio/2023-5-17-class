class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr) # eval()は文字列をPythonのコードとして評価する。
        except ZeroDivisionError:
            # muffledがTrueなら、ZeroDivisionErrorを無視する
            # muffledがFalseなら、ZeroDivisionErrorを発生させる
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise

mc = MuffledCalculator()
print(mc.calc("5/2"))
mc.muffled = True
print(mc.calc("5/0"))
mc.muffled = False
print(mc.calc("5/0"))