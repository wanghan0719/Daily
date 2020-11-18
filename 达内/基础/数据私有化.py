class Enemy:

    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

    @property
    # 读取私有数据
    def attack(self):
        return self.__attack

    # 输入是有数据
    @attack.setter
    def attack(self, value):
        if 0 <= value <= 100:
            self.__attack = value
        else:
            raise Exception('攻击力不合理')


em01 = Enemy('灭霸', 500)
