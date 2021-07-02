# decorator 裝飾器 加工
import time


'''
甚麼時候會用到decorator，
就是當你再改別人的程式或是API時或不太能動到的function，
想要對她做一些功能上的修改，
另外是decorator可以很清楚地知道你想要加裝那些功能
'''


# 傳遞function作為參數
def print_func(func):
    def inner():
        print('running', func.__name__)
        func()
    return inner


def time_func(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('elapsed', end - start, 'seconds')
    return inner


@print_func  # @print_func => test = print_func(test)的快寫
@time_func  # 可以疊加，等於把上面的@print_func裝飾到time_func
def test():
    for i in range(10000000):
        i = i + 1
    print('hi')


def test2():
    print('hi hi')


# 進行加工
# test()
# print('加工後')
# test = print_func(test)
# test = time_func(test)
#test2 = time_func(test2)
test()
# test2()
