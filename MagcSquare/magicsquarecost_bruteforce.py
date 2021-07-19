#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

#
# 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def formingMagicSquare(s):
    all_magicSquare_cost = []
    x=[1,2,3,4,5,6,7,8,9]
    for a in permutations(x,9):
        if a[0]+a[1]+a[2]==15 and a[3]+a[4]+a[5]==15:
            if a[6]+a[7]+a[8]==15 and a[0]+a[3]+a[6]==15:
                if a[1]+a[4]+a[7]==15 and a[2]+a[5]+a[8]==15:
                    if a[0]+a[4]+a[8]==15 and a[2]+a[4]+a[6]==15:
                        tmp_arr = [a[0:3], a[3:6], a[6:]]
                        #calculate cost
                        cost = abs(s[0][0] - a[0]) + \
                               abs(s[0][1] - a[1]) + \
                               abs(s[0][2] - a[2]) + \
                               abs(s[1][0] - a[3]) + \
                               abs(s[1][1] - a[4]) + \
                               abs(s[1][2] - a[5]) + \
                               abs(s[2][0] - a[6]) + \
                               abs(s[2][1] - a[7]) + \
                               abs(s[2][2] - a[8]) 
                        #print(cost)
                        #print()
                        all_magicSquare_cost.append(cost)
    return min(all_magicSquare_cost)   
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
