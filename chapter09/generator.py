def animal_generator():
    print("一つ目")
    yield "cat"
    print("二つ目")
    yield "dog"
    print("三つ目")
    yield "horse"


animal = animal_generator() # インスタンス化
# animal自体はオブジェクト
# print(next(animal)) # nextで呼び出すことができる catっていうとこまで処理する 関数を止める　catまで
# nextで区切ることができるっていうのがジェネレーターの役割(機能)
# print(next(animal)) # 二つ目 dogが実行される
# print(type(animal))

# for文でanimal_generatorの内容を全部回すことができる
for a in animal:
    print(a)