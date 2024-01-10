#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    arr = []
    ar = sorted(list(set(a)))
    for i in range(len(ar) - 1):
        arr.append(a.count(ar[i]))
        if abs(ar[i] - ar[i + 1]) == 1:
            arr.append(a.count(ar[i]) + a.count(ar[i+1]))
    arr.append(a.count(ar[len(ar) - 1]))
    return max(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
