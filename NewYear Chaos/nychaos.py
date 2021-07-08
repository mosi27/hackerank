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
    
    for i in range(q_len - 1, 0, -1):
        #where is i n bribed q
        curr_i = q.index(i + 1) 
        bribed = q[curr_i] - (curr_i + 1)
        #print("curr_i " + str(q[curr_i]) + "  at " + str(curr_i) + ", bribed " + str(bribed))
        
        if (bribed > 2):
           print("Too chaotic")
           return;
        elif (bribed == 0):
            continue
        else:
            m = curr_i
            my_range = -(bribed) if bribed < 0 else bribed
            for j in range(0, my_range):
                k = curr_i - j - 1 if bribed < 0 else curr_i + j + 1
                if q[k] < q[m]:
                    # swap
                    tmp = q[k]
                    q[k] = q[m]
                    q[m] = tmp
                    m = m + 1
                    tot_bribes = tot_bribes + 1
    print(tot_bribes)         

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

