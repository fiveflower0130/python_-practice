#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.


def hackerrankInString(s):
    indices = 'hackerrank'
    j = 0
    if len(s) < len(indices):
        return 'NO'
    else:
        for i in range(len(s)):
            if s[i] == indices[j]:
                j += 1
                if j >= len(indices):
                    return "YES"
        return "NO"


s = 'knarrekcah'
test_lib = '''
    knarrekcah
    hackerrank
    hackeronek
    abcdefghijklmnopqrstuvwxyz
    rhackerank
    ahankercka
    hacakaeararanaka
    hhhhaaaaackkkkerrrrrrrrank
    crackerhackerknar
    hhhackkerbanker
'''
result = hackerrankInString(s)
print(result)
