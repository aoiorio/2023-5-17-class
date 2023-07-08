import PySimpleGUI as sg
# PySimpleGUIをimport(追加)


layout = [[sg.Text("Hello from PySimpleGUI")], 
        [sg.Text("GoodMorning from PySimpleGUI")], 
        [sg.Text("GoodMorning from PySimpleGUI"), sg.InputText()],] # テキストを入力

window = sg.Window('title', layout)
evnet, values = window.read()
window.close()
