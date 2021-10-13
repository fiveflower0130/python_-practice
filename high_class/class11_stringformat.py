# string format

#printf
name = 'Allen'
x = 10
y = 3.14
# print('hi %s' % name) # %是指回傳值 s指string
# print('hi %d' %  x) # d是指整數
# print('hi %f' %  y) # f是指浮點數
# print('hi %s, my nunber is %d' % (name, x)) 

# format用法
print('hi {}, my number is {}'.format(name, x))
# 也可以這樣在python 3.6+後 改為
print(f'hi {name}, my number is {x}')