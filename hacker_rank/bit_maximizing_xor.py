import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    num_range = []
    for a in range(l, r):
        for b in range(l+1, r+1):
            num_range.append(a^b)
    aa = [a^b for a in range(l, r) for b in range(l+1, r+1)]
    return max(aa)
    
            
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
