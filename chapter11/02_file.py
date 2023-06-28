some_file = open('some.txt', 'w+') # どんな形態にするか指定するread, write, r+ etc....

try: # for ぶんでsome_file
    for i in range(5):
        some_file.write(f'{i}Hello, Python\n')
finally:
    some_file.close() # file を