# import errorが出る時にはインタープリンタを変えてもいいかも（変えても直らない）
import PySimpleGUI as sg # PySimpleGUIをimport(追加)

# layoutを決める
layout = [[sg.Text("Hello from PySimpleGUI")],
        [sg.Text("GoodMorning from PySimpleGUI")],
        [sg.Text("GoodMorning from PySimpleGUI"), sg.InputText()],] # テキストを入力することが出来る

window = sg.Window('title', layout) # windowを表示する
evnet, values = window.read() # fileを読み込むコード
window.close() #ファイルを閉じるコード
