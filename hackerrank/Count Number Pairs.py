#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countAffordablePairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER budget
#

def countAffordablePairs(prices, budget):
    # Write your code here
    left = 0
    count = 0
    prices.sort()
    right = len(prices) - 1
    while left < right:
        if prices[left] + prices[right] <= budget:
            count += (right - left)
            left += 1
        else:
            right -= 1
    return count


if __name__ == '__main__':
    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    budget = int(input().strip())

    result = countAffordablePairs(prices, budget)

    print(result)
