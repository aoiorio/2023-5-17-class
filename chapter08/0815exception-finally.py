x = None
try:
    # ファイルを開く
    x = 1 / 1
except Exception as e:
    print("不正な入力です：", e)
    print("処理を継続します。")
finally: # 必ずtry の中が実行し終わったら、finally の中にあるやつを実行する
    # ファイルを閉じる
    print("後始末中・・・・・・・")
    del x
    
print("さらに処理を継続します。")
