#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    if n == len(c):
        return 0
    ar = []
    c = sorted(c)
    for i in range(len(c) - 1):
        ar.append((c[i+1] - c[i]) // 2)
    ar.append(c[0])
    ar.append(n - c[-1] - 1)
    return max(ar)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
