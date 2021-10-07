'''
property
是一種進階的用法，可以讓python達到使用OOP與private的功能
encapsulation 封裝 

getter method and setter method 用在 encapsulation private的用法
'''

# 一般程式寫法
class Batman:
    def __init__(self, hp):
        self._hp = hp

    # getter method
    def get_hp(self):
        print("getting hp......")
        return self._hp

    # setter method
    def set_hp(self, hp):
        self._hp = hp
        if hp > 100:
            self._hp = 100
        elif hp < 0:
            self._hp = 0
        else:
            self._hp = hp

b1 = Batman(100)
b2 = Batman(50)
b1.set_hp(b1.get_hp()+b2.get_hp())

# python寫法
class Batman1:
    def __init__(self, hp):
        self.hp = hp

    # getter method
    @property # 不是method的叫property，這裡是對method裝飾成property
    def hp(self):
        return self._hp

    # setter method
    @hp.setter
    def hp(self, hp):
        self._hp = hp
        if hp > 100:
            self._hp = 100
        elif hp < 0:
            self._hp = 0
        else:
            self._hp = hp

b1 = Batman1(100)
b2 = Batman1(50)
b1.hp = b1.hp + b2.hp