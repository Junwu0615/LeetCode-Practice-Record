#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    ret = []
    i = 0
    while i < n:
        char = s[i]
        count = 1
        while i + 1 < n and s[i + 1] == char:
            count += 1
            i += 1
        ret.append((char, count))
        i += 1

    ans = 0
    for char, count in ret:
        ans += count * (count + 1) // 2

    for i in range(1, len(ret) - 1):
        head = ret[i - 1]
        mid = ret[i]
        end = ret[i + 1]
        if mid[1] == 1 and head[0] == end[0]:
            ans += min(head[1], end[1])

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
