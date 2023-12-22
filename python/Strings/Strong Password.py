#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    special_characters = '!@#$%^&*()-+'
    arr = [0 for i in range(4)]
    for i in password:
        if i.isdigit() and arr[0] == 0:
            arr[0] = 1
        if i.islower() and arr[1] == 0:
            arr[1] = 1
        if i.isupper() and arr[2] == 0:
            arr[2] = 1
        if i in special_characters and arr[3] == 0:
            arr[3] = 1
    answer = 4 - sum(arr)
    if len(password) < 6:
        answer = 6 - len(password) if answer < 6 - len(password) else answer
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
