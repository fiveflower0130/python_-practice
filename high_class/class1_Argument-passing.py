#!/usr/bin/python
# -*- coding: utf-8 -*-

# namespace的層級說明
# L: local 低
# E: enclosed
# G: global
# B: built-in 高

# 如果參數是[]或{}系統會採用pass by reference
def f(y):  
    y[0] += 1


x = [0]
f(x)
print(x) # [0,1]


# 如果參數是一般則會採用pass by value
def ff(y):
    y += 1 # 動態連結dynamic bindin

x = 0
ff(x)
print(x) # 0

# 依照LEGB rule去尋找namespace

z = 1 
print(z)
def f():
    global z # 使用global會變成可以改變全域
    z = 2
    print(z)

f()

# nonlocal用法 用在function裡面的namespace變數改變
def g():
    y = 1
    def gg():
        nonlocal y
        y = 10
    ff()
    print(y)
f()
