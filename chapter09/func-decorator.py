# decorator

def sample(func): # funcにmyfuncが入ってくる @sampleに対してmyfuncを入れている
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

# a = sample(myfunc) と下に書いてあるコードは同じ
@sample# この@sampleの処理を装備するイメージ　myfuncに対して処理を装備する
def myfunc(): # myfuncはsampleで装飾されている
    print("myfunc") 
# クラスの恩恵を受けることができる
@sample
def main():
    print("main")

main() # classの引数の関数funcにmainを入れている
myfunc() # classの引数の関数funcにmyfuncを入れている