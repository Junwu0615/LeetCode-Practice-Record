#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    n = len(arr)
    max_num = -float("inf")
    for i in range(n - 2):
        for j in range(n - 2):
            head = sum(arr[i][j:j + 3])
            mid = arr[i + 1][j + 1]
            end = sum(arr[i + 2][j:j + 3])
            max_num = max(max_num, head + mid + end)
            # print(f"head: {head}")
            # print(f"mid: {mid}")
            # print(f"end: {end}")
    return max_num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
