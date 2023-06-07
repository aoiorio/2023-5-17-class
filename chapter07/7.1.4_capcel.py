# from {your_file_name} import {your_class_name}
from mod2 import openClass, sample
import math

obj = openClass()
obj.init(input("名前を入力してください："))
obj.set_name("settings")
objectName = obj.get_name()
obj.print_name()

obj2 = sample()
obj2.set_name("sample")
objectName2 = obj2.get_name()
print(objectName)