# Exception: 例外が発生している場所を確認する
def faulty(): # faulty = 欠陥
    raise Exception('例外が発生しました。')
def ignore_exception():
    faulty()

# faulty()のエラーを処理する
def handle_exception():
    try:
        faulty()
    except:
        print("例外が処理されました。")

handle_exception() # 例外が処理されました。
ignore_exception() # 例外が発生しました。
# faulty()