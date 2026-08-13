#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    # print(f"s: {s}")
    n = len(s)
    tmp = {}
    for i in range(n):
        for j in range(i+1, n+1):
            curr = "".join(sorted(s[i:j]))
            if curr not in tmp:
                tmp[curr] = 1
            else:
                tmp[curr] += 1
            # print(curr)
    # print(tmp)
    count = 0
    for i in tmp.items():
        if i[1] > 0:
            count += (i[1] * (i[1]-1) // 2)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
