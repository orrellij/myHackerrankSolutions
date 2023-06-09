#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    total = 0

# The line above sets the initial sum to be zero as a starting point.

# The lines below contain a loop that adds each number in the array
# one by one, and each time it adds a new value it stores it as the sum.

    for i in ar:
        total = i + total
    return total

# The below lines were added by Hackerrank. They take an input and
# make it into an array. They also take an input for the number of
# elements in the array. I was able to reuse my code for this 
# hacckerrank challenge.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()