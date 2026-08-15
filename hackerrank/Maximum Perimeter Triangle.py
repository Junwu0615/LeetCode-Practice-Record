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
    # print(f"sticks: {sticks}")
    sticks.sort()
    n = len(sticks)
    ret = [-1]
    max_num = 0

    if not sticks or n < 3:
        return ret

    for idx in range(n - 2):
        curr = sticks[idx : idx + 3]
        if curr[0] + curr[1] > curr[2]:
            _sum = max(curr)
            if _sum > max_num:
                max_num = _sum
                ret = curr
    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
