# import webbrowser

# webbrowser.open("https://en.wikipedia.org/wiki/Melonpan") # webブラウザを開くことができる

# import time

# now = time.localtime()
# print(now.tm_year, "年", now.tm_mon, "月", now.tm_mday, "日")

# import datetime
# date_now = datetime.datetime.now() # datetime.not()という関数を取得している
# print(date_now)

from random import shuffle, choice

values = list(range(1, 11)) + "J Q K".split()

suits = ["♢", "♤", "♡", "♧"]

deck = [f'{value, suit}' for value in values for suit in suits]
print(deck)
print('-' * 10)
print(shuffle(deck))

for n in range(5):
    print(choice(deck)) # choiceでランダムなカードを引いてくることができるdeckの中身の2つをchoiceする