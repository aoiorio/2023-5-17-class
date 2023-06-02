class Filter:
    def init(self):
        self.blocked = [1,2,3]
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked] # blockedの中に入っていない配列を返してくれる

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['eggs']

# main処理
f = Filter()
f.init()
print(f.filter([1, 2, 3])) # [1, 2, 3]
s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])) # ['eggs], 'bacon']
