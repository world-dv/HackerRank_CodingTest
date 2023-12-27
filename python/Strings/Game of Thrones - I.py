#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    dic = dict()
    for i in s:
        dic[i] = s.count(i)
    count = 0
    for i in dic:
        if dic[i] % 2 == 1:
            count += 1
    if len(s) % 2 == 0:
        return 'YES' if count == 0 else 'NO'
    return 'YES' if count == 1 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
