"""
Iterator 很像for但不同的是他不會一直執行，
每一次動作都只取一次值(__next()__)
iterator是有stateful狀態的，
他會記得每一次運行到哪的情況且一次只作完1 run的動作，
要繼續做下去就必須繼續next
不過要注意必須要知道他何時會出錯不然會當掉．

接著要說到Generator他跟Iterator很像
那何時會用到呢
Generator就是一個functon 他就是負責生產
而Iterator就是使用Generator來產生東西
每call一次Iterator就會執行Generator

所以

"""

x = [1, 2, 3]
print(dir(x)) # 會到有iter的屬性

it = x.__iter__()
print(dir(it)) # 會看到有next屬性

it_next = it.__next__()
print(it_next) # 就會看到1
print(it_next) # 就會看到2
print(it_next) # 就會看到3
print(it_next) # 這個會出現except error 因為只到3

# 每一次產生1給出去 yield是指生產的意思
def g():
    while True:
        yield 1

# print(next(g())) # 得到1
# print(next(g())) # 得到1
# print(next(g())) # 得到1

# generator的範例
'''
使用產生器的原因是多半為了避免浪費記憶體，
一般使用for會直接占用所有的記憶體但搭配generator的話可以一邊產出一邊執行，
以以下的案例來說當my_range產生一個數字後，才會餵給for執行

PS: python裡的range並不是generator因為range的回傳結果不是iterator，再來是不能使用next
'''
def my_range(n):
    i = 0
    while i < n:
        print(f"我要產生{i}了")
        yield i
        i += 1

for i in my_range(5):
    print(i)


# list comprehension ->清單快寫法
x = [0, 1, 2, 3, 4]
print([i*i for i in x])

# 如果將[]改為()則會變成generator expression
iter1 = (i*i for i in x)
iter2 = (i+2 for i in iter1)
print(next(iter2))
print(next(iter2))
print(next(iter2))