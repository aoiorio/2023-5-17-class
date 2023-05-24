# # # words = ['This', 'is', 'an', 'ex', 'parrot']
# # # for word in words:
# # #     print(word, end=" ")
# # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # for number in numbers:
# # #     print("My parrot name is ", number)
# # d = {}
# # for i in range(20):
# #     d[i] = i + 1
# # # d = {'x': 10, 'y': 2, 'z': 3}
# # for key in d:
# #     print(key, 'は', d[key], 'に対応')

# # for key in d.values():
#      print(key, 'は', 'に対応')


# names = ["渋谷", "恵比寿", "上野", "巣鴨"]
# ages = [15, 45, 32, 102]

# for name, age in zip(names, ages):
#     print(name, "さんは", ages, "歳です。")


strings = ["あいうえお", "xxxyyy", "axxβyyy"]
print(strings)
# index = 0
print(list(enumerate(strings)))
for index, string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '<検閲削除>'
    # index += 1
print(strings)