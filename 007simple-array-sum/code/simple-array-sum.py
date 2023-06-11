# This is everything that hackerrank had in the code already.

# Here it is required to import all these classes so we can use their
# methods.

import math
import os
import random
import re
import sys

# Here's where we define our function that sums the array.

def simpleArraySum(ar):
    total = 0           # Set the inital sum to zero.

    # This is the for loop that adds each value one at a time, storing
    # the value as 'total' each loop.
    
    for i in ar:
        
        total = total + i

    return total 

# This was already written by Hackerrank, it takes an input for the 
# number of elements in the array as well the actual values.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    
    ar_count = int(input().strip())

    ar = list(map(int,input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')
    
    fptr.close()
