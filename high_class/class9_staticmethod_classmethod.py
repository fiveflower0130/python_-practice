"""
@staticmethod
在創建一個class的時候如果要使用裡面的method不需要建立instance就可以直接使用，看例１
就是當成一般的function，只要沒有用到self就可以使用staticmethod

@classmethod
"""

# 例1
class Batman:
    
    def f(self):
        print("static method")

    @staticmethod
    def calc_avg(x):
        return sum(x)/len(x)
        f()
    
    @classmethod
    def ffffff(cls):
        cls().f()

x = [1, 2, 3]
print(Batman.calc_avg(x))