#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
#  n = 1246326493
#  n = 1384145241

def counterGame(n):
    # Write your code here
    # count = 0
    # power_2 = []
    # tmp_n = 1384145241
    # print(tmp_n)
    # while int(tmp_n) > 3:
    #     if int(tmp_n / 2 % 2) == 0:
    #         tmp_n = int(tmp_n / 2)
    #         count += 1
    #     else:
    #         k = 1
    #         while k < tmp_n:
    #             k = k * 2
    #         print(tmp_n, k)
    #         tmp_n = tmp_n - int(k/2)
    #         count += 1
    # print(count)
    # if count % 2 == 0:
    #     return "Louise"
    # else:
    #     return "Richard"
    n = bin(n)[2:]
    print(n)
    n = n.split('1')
    print(n)
    turns = len(n)+len(n[-1])-2
    print(turns)
    return 'Louise' if turns&1 else 'Richard'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
