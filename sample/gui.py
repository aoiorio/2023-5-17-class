import PySimpleGUI as sg # PySimpleGUIをsgとしてimportする

sg.theme("DarkBlue13")  # please make your windows colorful
layout = [
    [sg.Text("1から7の好きな数字を入力してください"), sg.Text(size=(12, 1), key="-OUTPUT-")], # keyでKeyを設定する(基本は英語の大文字みたい)
    [sg.Input(key="-IN-")],
    [sg.Button("Show")],
    [sg.Text("追加データを入力してください")],
    [sg.Text("商品"), sg.Input(key='-THING-'), sg.Text("商品コード"), sg.Input(key='-IN-')],
    [sg.Text('', key='-update-'), sg.Text('', key='-number-')],
    [sg.Button("Register"), sg.Button("Exit")], # Buttonを配置するコード
]
window = sg.Window("Window Title", layout)

while True:  # Event Loop
    event, values = window.read()  # ボタン押下等のイベントで値が取得される
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Show":
        # change the "output" element to be the value of "input" element
        window["-OUTPUT-"].update(values["-IN-"]) # OUTPUTの値をINの値に変える
    if event == "Register": # もしeventがRegisterになったらという条件式
        window["-update-"].update(f'{values["-THING-"]}が追加されました。') # Keyを設定したらそのKeyに対してアクションを起こすことができる

window.close() #ファイルを閉じる動作
