#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
   
def minimumBribes(q):
    q_len = len(q)
    org_q = range(q_len)
    tot_bribes = 0
    skip_idx = []
    for i,N in enumerate(q): 
        bribed = N - i
        if bribed > 3:
            print("Too chaotic")
            return   
            
        if (bribed > 0 and i + bribed <= q_len):
            sub_arr = q[i+1:i + bribed]
            for j,M in enumerate(sub_arr): 
                if M < N:
                    tot_bribes = tot_bribes + 1
        else:
            bribed = -(bribed)
            if (bribed != 0 and bribed - i <= 0):
                sub_arr = q[i-bribed:i+1]
                for j,M in enumerate(sub_arr): 
                    if M > N:
                        tot_bribes = tot_bribes + 1
                        
    print(tot_bribes) 
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))
        
        minimumBribes(q)
