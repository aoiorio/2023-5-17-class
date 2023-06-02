#　再帰
def factorial(n):
    # nが1の時、処理終了する
    if n == 1:
        return 1
    # nが1でない時、再帰呼び出しする
    return n * factorial(n - 1)

kaijou = factorial(int(input()))
print(kaijou)
