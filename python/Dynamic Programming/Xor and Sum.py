#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'xorAndSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
sys.set_int_max_str_digits(100000000)

def xorAndSum(a, b):
    # Write your code here
    answer = 0
    for i in range(314159 + 1):
        answer += a ^ (b << i)
    return answer % ((10 ** 9) + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input(),2)

    b = int(input(),2)

    result = xorAndSum(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
