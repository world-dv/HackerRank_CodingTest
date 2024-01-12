#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    w = sorted(w)
    answer = 1
    idx = 0
    limit = w[idx]
    while idx < len(w):
        if w[idx] > limit + 4:
            answer += 1
            limit = w[idx]
        idx += 1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
