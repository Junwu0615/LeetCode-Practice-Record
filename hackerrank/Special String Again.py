#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    blocks = []
    i = 0
    while i < n:
        char = s[i]
        count = 1
        while i + 1 < n and s[i + 1] == char:
            count += 1
            i += 1
        blocks.append((char, count))
        i += 1

    ans = 0
    for char, count in blocks:
        ans += count * (count + 1) // 2

    for i in range(1, len(blocks) - 1):
        if blocks[i][1] == 1 and blocks[i - 1][0] == blocks[i + 1][0]:
            ans += min(blocks[i - 1][1], blocks[i + 1][1])

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
