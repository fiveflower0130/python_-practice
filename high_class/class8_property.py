"""
property
是一種進階的用法，可以讓python達到使用OOP與private的功能
encapsulation 封裝 
getter method and setter method 用在 encapsulation private的用法

使用方式
1. 直接設計屬性為public
2. 如需要用到getter 和 setter概念method則使用@property
"""

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

# b1 = Batman(100)
# b2 = Batman(50)
# b1.set_hp(b1.get_hp()+b2.get_hp())

# python寫法
class Batman1:
    def __init__(self, hp):
        self.hp = hp

    # getter method
    @property # 不是method的叫property，這裡是對method裝飾成property 且裝飾的名字要相同ex：hp
    def hp(self):
        print(f"getter hp {self._hp}")
        return self._hp

    # setter method
    @hp.setter
    def hp(self, hp):
        if hp > 100:
            self._hp = 100
        elif hp < 0:
            self._hp = 0
        else:
            self._hp = hp

b1 = Batman1(100)
# b2 = Batman1(50)
# b1.hp = b1.hp + b2.hp
b1.hp = 70
b1.hp