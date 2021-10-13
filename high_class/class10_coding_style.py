import test

help(test)
# docstring => documentation

# module的docstring寫法
"""
在開頭就寫，這樣程式會默認這個docstring為module的註解

用法：
你的class or func可以使用.__doc__來呼叫 EX:(Batman.__doc__)

如果是module 怎是使用help，這樣會印出裡面所有用法，EX:
import Batman

help(Batman)
"""

# class的docstring寫法
class Batman:
    """
    在class的裡面開頭寫上
    這是Batman用法
    """

# function的docstring寫法
def f():
    """
    在function裡面開頭寫上
    """

print(Batman.__doc__)
