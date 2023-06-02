from mod import Person

#  インスタンスの生成
foo = Person()
print(foo) # person objectになってperson class の関数が使えるようになる
bar = Person()
foo.set_name('Justin Bieber')
bar.set_name('Lii Nas X')
foo.greet()
bar.greet()