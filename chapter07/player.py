class Player(): # クラス「冒険者（プレイヤー）」
    # インスタンスを生成した時に勝手に呼び出される
    def __init__(self, name, level, hp, mp, attack, defence):
        self.name = name
        self.level = level
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.attack = attack
        self.defence = defence
    # introd
    def introduction(self, opponent):
        print("私の名前は" + self.name + "。よろしくね" + opponent + "さん。")
    # status informationの関数
    def display_info(self):
        print("----status information----")
        print("名前： %s" % self.name)
        print("Level: %2d" % self.level)
        print("HP: %3d/%3d" % (self.hp, self.maxhp))
        print("MP: %3d/%3d" % (self.mp, self.maxmp))
        print("攻撃力：%3d" % self.attack)
        print("防御力：%3d" % self.defence)
    # ダメージを与える（x だけHPを減らす!!!）
    def damage(self, x):
        if x > self.hp:
            self.hp = 0
            print("%sに%dのダメージ！" % (self.name, x))
            print("%sはから尽きた..." % self.name)
        else:
            self.hp -= x
            print("%sに%dのダメージ！" % (self.name, x))
