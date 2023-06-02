def inc(x):
    return x + 1

foo = 10
foo += 1
foo = inc(foo)
print(foo)

# キーワード引数
# def hello_1(greeting='おはよう', name='折尾'):
#     print(greeting, name)

# hello_1('折尾', 'こんにちは')

# キーワード引数
# hello_1(name='折尾', greeting='こんばんは')
# hello_1()

# 可変長引数です
def hello_2(title, param3, *params):
    print(title, param3, params)





# def hello_2(title, *params, param3):
#     print(title, *params, param3)


# def hello_3(title, *params, param3):
#     print(title, *params, param3)
# エラーになる呼び出し
# hello_2('こんにちは', 'おはよう', 'さようなら')
# 良い例
hello_2('こんにちは', 'おはよう', 'さようなら', '売買')
# hello_3('こんにちは', 'おはよう', '売買', param3='hwo are you doing?')