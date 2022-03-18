'''
本節會說到如何使用python常用的內建函數
1. enumerate
2. lambda
3. map
4. filter
5. zip

'''
# 1. enumerate 索引功能 enumerate是一個iterator但不是generator
# x = ['a', 'b', 'c', 'd']

# for i, name in enumerate(x):
#     print(i, name)

# for i in range(len(x)):
#     print(i, x[i])

# 2. lambda 清單快寫法 lambda後面的x是一個宣告的暫時的變數值
# a = lambda x: x + 1
# print(a(1))

# tuple -> 內容是不能更改的因為裡面是一個iterator list則可以 
products = [
    ('摩卡咖啡', 145),
    ('麥香奶茶', 10),
    ('珍珠奶茶', 65)
]

products_1 = [
    ['摩卡咖啡', 145],
    ['麥香奶茶', 10],
    ['珍珠奶茶', 65]
]

# lambda常和sorted一起用 主要是他可以取得裡面幾層的值直接進行排序後傳回
# print(sorted(products, key=lambda x: x[1]))

# 如果裡面是dict在list裡也是可以進行lambda排序
p0 = {
    'name': '摩卡碎片咖啡',
    'price': 145,
}

p1 = {
    'name': '麥香奶茶',
    'price': 10,
}

p2 = {
    'name': '珍珠奶茶',
    'price': 65,
}

products_2 = [p0, p1, p2]
# print(sorted(products_2, key=lambda x: x['price']))


# 3. map->就是把清單list裡的東西都套上一樣的用法 會回傳一個iterator給你而不是清單
x = ['this', 'is', 'map']
print(list(map(len, x)))
# for i in map(len, x):
#     print(i)

# map 常常會跟list lambda一起用
y = [1, 2, 3, 4]
print(list(map(lambda i: i*i, y)))

# 4. filter -> 挑出你要的條件的數值後回傳
print(list(filter(lambda i: i < 3, y)))

# 下面寫法會等於上面的lambda i:i<3，變成用function取代
def f(x):
    if x > 2:
        return False
    else:
        return True

# 但現在大部分人都是使用list compertation而不是疊加法

# 5. zip 會將兩個list內的東西組合 會回傳iterator
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))
