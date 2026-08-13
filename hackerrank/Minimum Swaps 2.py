#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    n = len(arr)
    for i in range(n):
        while arr[i] != i + 1:
            target_idx = arr[i] - 1
            arr[i], arr[target_idx] = arr[target_idx], arr[i]
            swaps += 1

    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
