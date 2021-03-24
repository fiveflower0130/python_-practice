import math
import os
import random
import re
import sys

# candles_count = int(input().strip())
# print(candles_count)


# def square(x):
#     return int(x) ** 2


# data = input().rstrip().split()
# print(data)
# print(map(int, data))
# candles = list(map(int, data))
# print(candles)
# m = 5
# n = 4
# print(min(m, n)//2)
# indices = []
# for c in range(min(5, 4)//2):
#     index = []
#     print(c)
#     for i in range(c, n-c):
#         print(i)
#         index.append((c, i))
#     for i in range(c+1, m-1-c):
#         index.append((i, n-1-c))
#     for i in range(c, n-c)[::-1]:
#         index.append((m-1-c, i))
#     for i in range(1+c, m-1-c)[::-1]:
#         index.append((i, c))
#     print(index)
#     indices.append(index)
# print(indices)

# def find_max(lower, upper, badnumber):
#     data = []
#     new = []
#     for b in badnumber:
#         if b > lower and b < upper:
#             data.append(b)
#     data = sorted(data)
#     print("bad number list: ", data)
#     low = lower
#     if low < data[0]:
#         new.append([low, data[0]-1])
#     for i in range(len(data)):
#         if i+1 == len(data):
#             low = data[i]+1
#             new.append([low, upper])
#         else:
#             low = data[i]+1
#             up = data[i+1]-1
#             if low <= up:
#                 new.append([data[i]+1, data[i+1]-1])
#     print("range: ",new)
#     max_number = [n[1]-n[0]+1 for n in new]
#     print(max_number)
#     print(max(max_number))


# lower = 3
# upper = 60
# badnumber = [5, 4, 2, 15, 11, 30, 19, 24, 37, 48, 44, 58]
# find_max(lower, upper, badnumber)

# def removestr(s, t):
#     data = s
#     count = 0
#     while True:
#         if t in data:
#             count += 1 
#             print(data)
#             data = data.replace(t,'',1)
#         else:
#             break
#     print(count)
#     print(data)

# s = 'aaaabbbbbaabb'
# t = 'ab'
# removestr(s, t)

# save
