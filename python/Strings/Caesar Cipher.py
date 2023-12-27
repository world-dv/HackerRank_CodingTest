#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    answer = ''
    for i in s:
        if i.isalpha():
            a = ord(i) + (k % 26)
            if i.isupper():
                a = chr(a) if a <= ord('Z') else chr(a - 26)
            if i.islower():
                a = chr(a) if a <= ord('z') else chr(a - 26)
            answer += a
        else:
            answer += i
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
