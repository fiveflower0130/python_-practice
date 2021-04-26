import random

while True:
    start = int(input("please input your start value: "))
    end = int(input("please input your end value: "))
    if start <= 0 or start > end:
        print("incorrect value for start, please try again!")
    elif end <= 0 or end < start:
        print("incorrect value for end, please try again!")
    else:
        break
r = random.randint(start, end)
count = 0
while True:
    a = int(input(f'please input a number between {start} - {end}: '))
    if a >= start and a <= end:
        count += 1
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
    else:
        print(
            f'The number is wrong, it should between {start} - {end} , please retry again')
