#!/bin/python3

import math
import os
import random
import re
import sys

#
# 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def hourglassSum(arr):
    sums = []    
    rows = len(arr)
    cols = len(arr[0]) if (rows > 0) else 0
    
    for i in range(1, rows):
        for j in range(1, cols):
            # check row_max and col_max
            col_max = j + 2
            row_max = i + 2
            if row_max <= rows and col_max <= cols:
                total_sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j]  + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
                sums.append(total_sum)
    sums.sort(reverse = True)
    return sums[0]        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
