#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findZeroSumTripletsInWindow' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY readings
#  2. INTEGER windowSize
#

def findZeroSumTripletsInWindow(readings, windowSize):
    # Write your code here
    n = len(readings)
    res_set = set()

    if windowSize < 3 or n < windowSize:
        return []

    for i in range(n - windowSize + 1):
        window = readings[i: i + windowSize]
        window.sort()
        w_len = len(window)

        for j in range(w_len - 2):
            # if j > 0 and window[j] == window[j - 1]:
            #     continue

            left = j + 1
            right = w_len - 1

            while left < right:
                _sum = window[j] + window[left] + window[right]

                if _sum == 0:
                    triplet = (window[j], window[left], window[right])
                    res_set.add(triplet)

                    # while left < right and window[left] == window[left + 1]:
                    #     left += 1
                    # while left < right and window[right] == window[right - 1]:
                    #     right -= 1

                    left += 1
                    right -= 1

                elif _sum < 0:
                    left += 1
                else:
                    right -= 1

    return [list(t) for t in res_set]


if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = int(input().strip())
        readings.append(readings_item)

    windowSize = int(input().strip())

    result = findZeroSumTripletsInWindow(readings, windowSize)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
