from high_class.class3_dunder_methods import Products  # parent class / base class

# child class / derived class


class Drinks(Products):  # 直接繼承Products裡的function，如果用到init則會直接取代parent class裡的init
    # override
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume


'''
class Food(Products):
    pass
# 可以寫成以下的方法
Food = type('Food', (Products, ), {})
f = Food('麵包', 50)
print(type(f))
print(isinstance(f, Food))
print(isinstance(Food, type))
print(isinstance(type, object))
# 從此得知type可以產生一個class的instance(實例)
# type則是object裡的一個instance(實例)
# type也是一個metaclass(製作class的框架)
'''

d = Drinks('白芋珍珠奶茶', 70, 750)
print(d.volume)
print(type(d))
print(isinstance(d, Drinks))
print(isinstance(d, Products))
