from tkinter import *

def callback(event): # マウスがクリックされたりとかactionが起こった時にcallbackが渡される
    print(event)
    print(event.x, event.y)
# ユーザーが行った処理に対して、eventという引数を渡している

top = Tk() # インスタンス化 topという変数にtkinterのTk()を代入これがオブジェクト？？
top.geometry("400x300") # 幅を指定
top.bind('<Button-1>', callback)

top.mainloop()
