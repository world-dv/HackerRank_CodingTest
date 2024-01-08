#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    check = 0
    for i in range(p, q + 1):
        a = str(i ** 2)
        if i == 1:
            print(i, end=' ')
            continue
        if len(a) > 1 and i == int(a[:len(a)//2]) + int(a[len(a)//2:]):
            check = 1
            print(i, end=' ')
    if check == 0:
        print('INVALID RANGE')
            
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
