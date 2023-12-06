#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    answer = s[:-2]
    if s[-2] == 'A' and s[:2] == '12':
        answer = '00' + s[2:-2]
    if s[-2] == 'P' and s[:2] != '12':
        answer = str(int(s[:2]) + 12) + s[2:-2]
    return answer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
