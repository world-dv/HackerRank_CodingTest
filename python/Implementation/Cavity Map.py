#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    if len(grid) == 1:
        return grid
    answer = ['' for j in range(len(grid))]
    answer[0] = grid[0]
    answer[-1] = grid[-1]
    for i in range(1, len(grid)-1):
        answer[i] += grid[i][0]
        for j in range(1, len(grid[i])-1):
            a = int(grid[i][j])
            if a > int(grid[i-1][j]) and a > int(grid[i+1][j]) and a > int(grid[i][j-1]) and a > int(grid[i][j+1]):
                answer[i] += 'X'
            else:
                answer[i] += grid[i][j]
        answer[i] += grid[i][-1]
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
