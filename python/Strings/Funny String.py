#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    answer = []
    arr = [ord(i) for i in s]
    for i in range(0, len(arr) - 1):
        answer.append(abs(arr[i] - arr[i+1]))
    if answer == answer[::-1]:
        return 'Funny'
    return 'Not Funny'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
