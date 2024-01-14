#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    for i in b:
        if i != '_' and b.count(i) == 1:
            return 'NO'
    if '_' not in b:
        answer = 0
        for i in range(len(b) - 1):
            if b[i] == b[i+1]:
                answer = 1
            else:
                if answer == 1:
                    answer = 0
                else:
                    return 'NO'
    return 'YES'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
