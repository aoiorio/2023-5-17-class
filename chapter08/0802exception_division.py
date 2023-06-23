try:
    x = int(input("最初の数を入力してください。"))
    y = int(input("二番目の数を入力してください")) 
    print(x/y)

# except (ZeroDivisionError, ValueError, NameError) as e:
#     print(e)
# except (ZeroDivisionError, ValueError):
#     print("値が不正です")
except ZeroDivisionError:
    print("0で割ることはできません")
except ValueError:
    print("数値を入力してください")
    # print("二番目の数に0以外を入力してください！")
# except ValueError:
#     print("数値を入力してください。", n)
print("=====END=====")