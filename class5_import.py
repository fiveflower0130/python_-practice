import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1
    a = int(input('please input a number between 1 - 100: '))
    if a == r:
        print(f'answer is {r}, you got it!')
        print(f'You have guess {count} times!')
        break
    elif a > r:
        print('Your number is higher than answer!')
    elif a < r:
        print('Your number is lower than answer!')
    else:
        print('something is wrong!')
