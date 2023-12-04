#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count_0 = 0
    count_plus = 0
    count_minus = 0
    for i in arr:
        if i == 0:
            count_0 += 1
        if i > 0:
            count_plus += 1
        if i < 0:
            count_minus += 1
    print("%0.6f" % (count_plus / n))
    print("%0.6f" % (count_minus / n))
    print("%0.6f" % (count_0 / n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
