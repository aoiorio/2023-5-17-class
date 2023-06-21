def sample(myfunc):
    print("It's a decorator")
    return myfunc

@sample # この@sampleの処理を装備するイメージ　myfuncに対して処理を装備する
def myfunc():
    pass

myfunc()