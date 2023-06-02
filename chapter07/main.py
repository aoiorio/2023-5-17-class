class Pokemon:
    def __init__(self, name, hp, type):
        self.name = name
        self.hp = hp
        self.type = type
    def getName(self):
        return self.name
    def getHp(self):
        return self.hp
    def getType(self):
        return self.type
    def damage(self, damage):
        self.hp -= damage
    def printInfo(self):
        print(f"{self.name}は、{self.type}タイプ。HPは{self.hp}です。")
    

        
pikatyu = Pokemon("ピカチュウ", 100, "でんき")
hitokage = Pokemon("ヒトカゲ", 50, "ひ")
pikatyu.printInfo() #ピカチュウのタイプやHPを表示してくれる
hitokage.printInfo() # ヒトカゲのタイプやHPを表示してくれる
    
# monsterName1 = "ピカチュウ"
# monsterName2 = "ヒトカゲ"

print(f"{pikatyu.getName()}は、攻撃した！")
hitokage.damage(10)
print(f"{hitokage.getName()}は、10のダメージを受けた！　残り：{hitokage.getHp()}")

print(f"{hitokage.getName()}は、攻撃した！")
pikatyu.damage(20)
print(f"{pikatyu.getName()}は、20のダメージを受けた！　残り：{pikatyu.getHp()}")