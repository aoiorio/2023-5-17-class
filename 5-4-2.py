#name = input("お名前は？：")
#if name.endswith("葵"):
#    print('こんにちは、' + name)
#else:
#    print("初めまして。")
    #name2 = input("知りませんね。じゃあ、誰ですか？：")
    #if name2.endswith("一平"):
        #print("はじめまして。" + name2)
#status = "友人" if name.endswith("一平") else "他人"
#print(status)

#num = float(input('数を入力してください：　'))
#if num > 0:
#   print("整数です")
#elif num < 0:
#    print("負の数です")
#else:
#    print("0です")

name = input('May I have your name?')
if name.endswith('Aoi'):
    if name.startswith("Mr."):
        print("Hello, Mr. Aoi!")
    elif name.startswith("Mrs."):
        print("Hello, Mrs. Aoi!")
    else:
        print("Hello, Aoi!")
else:
    print("Hello, stranger.")
    