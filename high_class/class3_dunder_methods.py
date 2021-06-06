#!/usr/bin/python
# -*- coding: utf-8 -*-

class Products:
    def __init__(self, name, price): # 1.初始化的dunder method
        self.name = name # property
        self.price = price # property

    def __str__(self): # 2.簡易印出用的dunder method
        return f'{self.name} ${self.price}' # f-string無法在python2上用喔

    #representation->代表回傳的字串要足以代表這個物件object
    def __repr__(self): # 3.完整回傳印出的dunder method 
        return f'<Products({self.name}, {self.price})>'

    def __add__(self, other): # 4.加法運用的dunder method
        if isinstance(other, str): #isinstance也是一種dunder method用於檢查str或其他
            self.name += other
        if isinstance(other, Products):
            return [self, other]

    def __mul__(self, other):
        re = []
        if isinstance(other, int):
            for i in range(other):
                re.append(self)
        return re

p = Products('珍珠奶茶', 60) # instance實例

# str跟repr可以只寫一種就好，如果都有寫會優先使用str

print(p)
print(repr(p))

# 測試add->只要看到＋這個符號就會呼叫__add__
p1 = Products('鮮奶茶', 60)
p2 = Products('義大利麵', 200)
print(p1 + p2)

# 測試mul
print(p1 * 5)

class ShoppingCart:
    def __init__(self, products):
        self.products = products
    
    def __getitem__(self, key):
        return self.products[key]

s = ShoppingCart([p1, p2])
print(s[1])