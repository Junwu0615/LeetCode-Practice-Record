#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    # print(f"k: {k}")
    # print(f"contests: {contests}")
    count = 0
    ret = []
    for num, luck in contests:
        if luck == 0:
            count += num
        else:
            ret += [num]
    # print(f"count: {count}")
    # print(f"ret: {ret}")
    ret.sort(reverse=True)
    return count + sum(ret[:k]) - sum(ret[k:])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
