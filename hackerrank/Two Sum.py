#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findTaskPairForSlot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY taskDurations
#  2. INTEGER slotLength
#

def findTaskPairForSlot(taskDurations, slotLength):
    # Write your code here
    if not taskDurations or len(taskDurations) < 2:
        return [-1, -1]

    record_dict = {}
    for idx, num in enumerate(taskDurations):
        diff = slotLength - num
        if diff in record_dict:
            return [record_dict[diff], idx]
        record_dict[num] = idx

    return [-1, -1]


if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))
