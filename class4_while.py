# 第一種99乘法
# a = 1
# b = 1
# while a < 10:
#     b = 1
#     while b < 10:
#         print(f'{a} X {b}')
#         b = b + 1
#     a = a + 1

# 第二種寫法
# a = 1
# while True:
#     if a < 10:
#         b = 1
#         while b < 10:
#             print(f'{a} X {b}')
#             b = b + 1
#         a = a + 1
#     else:
#         break
# while True:
#     name = input('please input your name: ')
#     if name == 'q':
#         break
retry = 3
while True:
    password = input('please input password: ')
    if password == 'a123456':
        print('login success!!')
        break
    else:
        retry = retry - 1
        if retry > 0:
            print(f'incorrect password! You have {retry} times rerty')
        else:
            print('Sorry, you have type wrong password for 3 times')
            break
