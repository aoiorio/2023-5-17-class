some_file = open('some.txt', 'r+') # どんな形態にするか指定するread, write, r+ etc....

# ls = some_file.readline()
# print(ls)
#  print(some_file.read()) # 最初に読み込んでしまうと次の文が末尾に追加されてしまう


# try: # for 文でsome_file
#     for i in range(5):
#         some_file.write(f'{i}Hello, Python\n')
# finally:
#     some_file.close() # file をclose(閉じる)
with open('some.txt', 'r+', encoding='utf-8') as some_file: #　as で変数名を決める, in this case, some_fileが変数名 (is variable)
    # for i in range(4):
    #     some_file.write(f'{i}:あいうえお!\n')
    for line in some_file:
        print(line, "test", end='')
    
        # 使うファイルが増えた時もその分増やせばいい どこでcloseするのかを気にしなくていいのでwithが楽
        # 文字化けする場合はencoding='utf-8'で文字コードを指定する