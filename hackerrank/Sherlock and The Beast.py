#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Write your code here
    y = 0
    while y <= n:
        x = n - y
        if x % 3 == 0:
            print("5" * x + "3" * y)
            return
        y += 5
    print("-1")


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
