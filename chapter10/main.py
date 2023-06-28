# import hello # ファイル名でimportできる
# from hello import hello_def, hello_def2　どの関数を使うのかを指定できる
# helloの中の関数を全て使うことができる
from hello import * # 全ての関数をimport できる [file name].[function name]と指定しなくてもいい
# hello の関数を呼び出したい時はimport で呼び出すことができる
# hello_def()
# hello_def2()

hello_def()
hello_def2()

# importされるときに実行されている関数も取り込んでしまう
# 例えば Hello, test!
print(__name__)