#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    # Write your code here
    max_num = 0
    n = len(calorie)
    calorie = sorted(calorie, reverse=True)
    for idx in range(n):
        max_num += 2 ** idx * calorie[idx]
    return max_num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
