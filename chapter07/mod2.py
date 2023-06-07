class openClass():
    def init(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def print_name(self):
        print(f"名前は、{self.name}です。")

class sample():
    def init(self):
        self.__name = "sample"
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
