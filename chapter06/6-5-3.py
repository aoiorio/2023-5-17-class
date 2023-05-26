def hello_4(name='皆さん', greeting='こんにちは'):
    print(name, greeting)

dic = {'name': '折尾', 'greeting': "hello What's up man?"}
hello_4(**dic)
hello_4(name='折尾', greeting="hello What's up man?")