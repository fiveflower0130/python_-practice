import math
import os
import random
import re
import sys

candles_count = int(input().strip())
print(candles_count)


def square(x):
    return int(x) ** 2


data = input().rstrip().split()
print(data)
print(map(int, data))
candles = list(map(int, data))
print(candles)
