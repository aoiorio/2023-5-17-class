
some_file = open('some.txt', 'r')

# print(some_file.read()2
# print(some_file.write("Hello python!!!!!!!!!!!!!!!!!!!!!!"))

# print(some_file.read())
# print(some_file.readline(1)) # ()の中に数字を入れると文字数単位で出力する値を指定できる
print(some_file.readlines(2))
some_file.close()