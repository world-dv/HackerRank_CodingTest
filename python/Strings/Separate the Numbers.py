#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    start = 0
    i = 0
    for i in range(1, len(s)):
        a = len(s[:i])
        if int(s[:i]) == int(s[i:i+a]) - 1 or int(s[:i]) == int(s[i:i+a+1]) - 1:
            start = s[:i]
    
    a = ''
    b = 0
    while True:
        a = a + str(int(start) + b)
        len_a = len(a)
        if s[:len_a] != a:
            break
        if len_a >= len(s):
            break
        b += 1
    if a != s:
        print('NO')
    else:
        print('YES ' + start)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
