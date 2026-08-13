#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    # print(f"k: {k}")
    # print(f"c: {c}")
    idx = 0
    count = 0
    c.sort(reverse=True)
    tmp = {i: 0 for i in range(k)}
    for i in c:
        if idx >= k:
            idx = 0
        # print(f"i: {i}, idx: {idx}, tmp[idx]: {tmp[idx]}")
        count += (tmp[idx] + 1) * i
        tmp[idx] += 1
        idx += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
