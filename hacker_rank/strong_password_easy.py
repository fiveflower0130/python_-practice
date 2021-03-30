#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    num = 0
    l = 0
    u = 0
    s = 0
    total = 0
    for i in password:
        if i in numbers:
            num = 1
        if i in lower_case:
            l = 1
        if i in upper_case:
            u = 1
        if i in special_characters:
            s = 1
    total = 4-sum([num, l, u, s])
    print(total)
    if n < 6:
        return max(6-n, total)
    else:
        return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
