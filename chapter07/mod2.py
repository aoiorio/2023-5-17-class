class openClass():
    name = "";
    __age = 0;
    def init(self, name, age):
        self.name = name
        self.__age = age

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
