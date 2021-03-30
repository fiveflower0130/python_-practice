#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.


def alternate(s):
    words = list(set(s))
    words.sort()
    keep_words = []
    count = 0
    print(words)
    for i in range(len(words)):
        count += 1
        for j in range(len(words)):
            if j+count < len(words):
                keep_words.append([words[i], words[j+count]])
    print(keep_words)
    clean_words = []
    for keep_word in keep_words:
        tmps = s
        for word in words:
            if word not in keep_word:
                tmps = tmps.replace(word, '')
        clean_words.append(tmps)
    print(clean_words)
    result_words = []
    for cc in clean_words:
        overlapping = 0
        for k in range(len(cc)):
            if k+1 < len(cc):
                if cc[k] == cc[k+1]:
                    overlapping += 1
        if overlapping < 1:
            result_words.append(cc)
    if len(result_words) > 0:
        return max([len(num) for num in result_words])
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
