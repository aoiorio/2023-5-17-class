#　再帰
def factorial(n):
    # nが1の時、処理終了
    if n == 1:
        return 1
    # nが1でない時、再帰呼び出しす
    return n * factorial(n - 1)

kaijou = factorial(3)
print(kaijou)
