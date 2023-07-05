from tkinter import * # Tkinterというモジュールをimportする

def click(): # クリックした時の動作をここで指定している
    print("You clicked it!")

top = Tk() # インスタンス化 topという変数にtkinterのTk()を代入これがオブジェクト？？

top.geometry("400x300")
btn = Button(text="click", command=click).pack() # 簡潔にpackができる
# btn.pack() # ボタンをウィンドウに表示するよっていう処理　ボタンを作ったらpackを実行させてあげてください

hello_label = Label(text="Hello").pack()
# second = Toplevel()
# second_label = Label(second, text="Second").pack() # 違うウィンドウで表示される
top.mainloop()
