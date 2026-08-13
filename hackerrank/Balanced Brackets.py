#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    if not s:
        return "NO"
    mapping = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    ret = []
    for i in s:
        if i not in mapping:
            ret += [i]
        else:
            if not ret or ret.pop() != mapping[i]:
                return "NO"

    if len(ret) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
