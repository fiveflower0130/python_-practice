import random

r = random.randint(1, 100)
while True:
    a = int(input('please input a number between 1 - 100: '))
    if a == r:
        print(f'r = {r}, you got it!')
        break
    elif a > r:
        print('Your number is higher than answer!')
    elif a < r:
        print('Your number is lower than answer!')
    else:
        print('something is wrong!')
