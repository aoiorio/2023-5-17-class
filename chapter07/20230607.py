class SimpleData:
    
    def __init__(self):
        self.a = 0
        self.b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __del__(self):
        print('インスタンスが破棄されました')

    def sum(self):
        return self.a + self.b
    
    def set(self, a, b):
        self.a = a
        self.b = b

class ComplexData(SimpleData):
    
    def __init__(self):
        super().__init__()
        self.c = 1
    
    def __init__(self, a, b):
        super().__init__(a, b)
        self.c = 1
    
    def sum(self):
        return self.a + self.b + self.c
    
    

data1 = SimpleData(1, 2)
print(data1.sum())
data1 = None





