#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#
sys.set_int_max_str_digits(10000000)
def extraLongFactorials(n):
    # Write your code here
    if n == 1 or n == 0:
        return n
    else:
        return n * extraLongFactorials(n-1)

if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))
    
