# import hello # ファイル名でimportできる
# from hello import hello_def, hello_def2　どの関数を使うのかを指定できる
from hello import * # 全ての関数をimport できる [file name].[function name]としなくてもいい
# hello_def()
# hello_def2()

# hello_def()
# hello_def2()

# importされるときに実行されている関数も取り込んでしまう
# 例えば Hello, test!
print(__name__)