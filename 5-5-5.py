# # from math import sqrt
# # print(list(range(99, 0, -1)))
# # for n in range(9, 0, -1):
# #     root = sqrt(n)
# #     if root == int(root):
# #         print(n)
# #         break

# seq = [1,2,3,4,5,6]
# for x in seq:
#     if x == 3: 
#         continue
#     print(x)

# word = input("単語を入力してください： ")
while True:
    word = input('単語を入力してください: ')
    print(not word)
    if not word: 
        break
    # 入力された単語に対して何か処理をする
    print(f'単語は、「{word}」でした！　あなたは、「{word}」な人物です。')