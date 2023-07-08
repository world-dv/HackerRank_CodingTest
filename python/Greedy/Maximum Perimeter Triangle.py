#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    answer = []
    arr = sorted(sticks, reverse=True)
    for i in range(len(arr)):
        k = arr[i]
        for j in range(i+1, len(arr) - 1):
            for z in range(j + 1, len(arr)):
                if k < arr[j] + arr[z]:
                    answer.append(arr[z])
                    answer.append(arr[j])
                    answer.append(k)
                    return answer 
               
    return answer or [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
