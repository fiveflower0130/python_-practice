'''  
1. closure 閉包(偷渡) -> 當func裡面有巢狀func時可以把enclosed的值給封裝打包出來
2. 這是一個偷渡的行為也是python獨有的用法
3. closure 裡面可以打包的東西很多 不管是 class function int string list都可以
4. 甚麼時候會用到closure，就是當你在使用decorator的時候，或是想使用global veriable的時候可以使用closure代替
'''

def f():
    x = 1
    y = 1

    def qqq():
        print("dsadascasasas")
    
    class SuperMan:
        def __init__(self):
            print('I am super man!')

    def inner():
        print(x)
        print(y)
        qqq()
        s = SuperMan()

    return inner

v = f()
print(v.__closure__)
#y()