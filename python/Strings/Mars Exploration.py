#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    answer = 0
    for i in range(0, len(s), 3):
        if s[i] != 'S':
            answer += 1
        if s[i+1] != 'O':
            answer += 1
        if s[i+2] != 'S':
            answer += 1
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
