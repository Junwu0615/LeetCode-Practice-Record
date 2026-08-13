#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTopKFrequentEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY events
#  2. INTEGER k
#

def getTopKFrequentEvents(events, k):
    # Write your code here
    tmp = {}
    for i in events:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
    return [i[0] for i in sorted(tmp.items(), key=lambda x:x[1], reverse=True)][:k]


if __name__ == '__main__':
    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    k = int(input().strip())

    result = getTopKFrequentEvents(events, k)

    print('\n'.join(map(str, result)))
