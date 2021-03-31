#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.


def caesarCipher(s, k):
    ori1 = 'abcdefghijklmnopqrstuvwxyz'
    ori2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    trans1 = ori1[k:]+ori1[:k]
    trans2 = ori2[k:]+ori2[:k]
    tmps = ''
    for i in range(len(s)):
        if s[i].islower():
            if s[i] in ori1:
                pos = ori1.index(s[i])
                tmps += trans1[pos]
        elif s[i].isupper():
            if s[i] in ori2:
                pos = ori2.index(s[i])
                tmps += trans2[pos]
        else:
            tmps += s[i]
    return tmps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
