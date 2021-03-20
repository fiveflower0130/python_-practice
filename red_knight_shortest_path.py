#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the printShortestPath function below.
def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    tmp_i = i_start
    tmp_j = j_start
    tmp_way = ""
    # walk_path = []
    count = 0
    while True:
        # walk_path.append([tmp_j, tmp_i])
        if count < n:
            if tmp_j == j_end and tmp_i != i_end:
                if tmp_i < i_end:
                    tmp_i = tmp_i + 2
                    if(tmp_j <= n/2):
                        tmp_j = tmp_j + 1
                        tmp_way += "LR "
                    else:
                        tmp_j = tmp_j - 1 
                        tmp_way += "LL "
                elif tmp_i > i_end:
                    tmp_i = tmp_i - 2
                    if(tmp_j <= n/2):
                        tmp_j = tmp_j + 1
                        tmp_way += "UR "
                    else:
                        tmp_j = tmp_j - 1
                        tmp_way += "UL "
            elif tmp_i == i_end:
                if tmp_j < j_end:
                    tmp_j = tmp_j + 2
                    tmp_way += "R "
                elif tmp_j > j_end:
                    tmp_j = tmp_j -2 
                    tmp_way += "L "
                else:
                    if tmp_j == j_end:
                        print(count)
                        print(tmp_way)
                        break;         
            elif tmp_i < i_end and tmp_j < j_end:
                tmp_i = tmp_i + 2
                tmp_j = tmp_i + 1  
                tmp_way += "LR "  
            elif tmp_i < i_end and tmp_j > j_end:
                tmp_i = tmp_i + 2
                tmp_j = tmp_j - 1
                tmp_way += "LL "
            elif tmp_i > i_end and tmp_j < j_end:
                tmp_i = tmp_i - 2
                tmp_j = tmp_j + 1
                tmp_way += "UR "
            elif tmp_i > i_end and tmp_j > j_end:
                tmp_i = tmp_i - 2
                tmp_j = tmp_j - 1
                tmp_way += "UL "
        else:
            print("Impossible")
            break
            
        count += 1
        
                
            

if __name__ == '__main__':
    n = int(input())

    i_startJ_start = input().split()

    i_start = int(i_startJ_start[0])

    j_start = int(i_startJ_start[1])

    i_end = int(i_startJ_start[2])

    j_end = int(i_startJ_start[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)