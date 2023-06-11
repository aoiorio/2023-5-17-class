try:
    print("簡単な仕事") # 簡単なお仕事
    raise Exception("error") # エラーが発生しました
except:
    print("エラーが発生しました。")
else:
    print("処理正常")
# そうですね