#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    arr = []
    hackerrank = 'hackerrank'
    for i in s:
        if i in hackerrank:
            if i not in arr:
                arr.append(i)
            elif (i == 'a' or i == 'k' or i == 'r') and i in arr:
                arr.append(i)
            if arr[-1] != hackerrank[len(arr)-1]:
                arr.pop()
        if ''.join(arr) == hackerrank:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

