#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    count = 0
    answer = 0
    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break
    answer = len(s) - count + len(t) - count
    if count == len(s) and (len(t) - count) % 2 != 0:
        answer += 2 * count + 1
    return 'Yes' if answer <= k else 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
