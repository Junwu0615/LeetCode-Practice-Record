#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    H = len(matrix)
    W = len(matrix[0])
    max_area = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= H or j >= W or matrix[i][j] == 0:
            return 0

        matrix[i][j] = 0
        count = 1

        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                count += dfs(i + x, j + y)

        return count

    for i in range(H):
        for j in range(W):
            if matrix[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
