#!/usr/bin/python
# -*- coding: utf-8 -*-

# python的底線會有5種情況
# _
# _name
# name_
# __name
# __name__

# 第一種_ ->不重要的參數就可以用_代替
for _ in range(10): # _可以表示i或其他變數
    print(_, 'hi')

name, _ = 'name$age'.split('$') 
# 對name&age做擷取然後只存取name age則忽視（所以用_代替）

# 第二種 用在private (naming convention)
class Qwe:
    def public_function(self):
        print("public function")

    # helper function
    def _private_function(self):
        print('private fuction')
q = Qwe()
# q.public_function()
q._private_function() # 即使是private也可以用（應該不行才對）

# 但如果是直接寫一個function 被import而不是寫在class裡面就會有private功能
# 一定要用from xxx import xxx的方式才會有用

# 第三種 避開已經使用過的或是不能用namespace則是在後面加上_
x = 5
x_ = 5

def d():
    print("123")

def d_():
    print("1234")

# 第四種 避免自動重新命名
class Person:
    def __init__(self):
        self.x = 1
        self._y = 1
        self.__z = 1

p = Person()
print(p.x)
print(p._y)
print(dir(p)) # 會看到 self.__z已被改為_Person__z

# 第五種 初始化的function 可以叫做 dunfer methods / magic methods

