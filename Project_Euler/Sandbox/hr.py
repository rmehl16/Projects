#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    ht1 = sum(h1)
    ht2 = sum(h2)
    ht3 = sum(h3)
    
    # All heights equal
    if ht1 == ht2 and ht2 == ht3:
        return ht1
    
    if max(ht1, ht2, ht3) == ht1:
        #print(f'Length of h1 before pop {len(h1)}')
        h1.pop(0)
    elif max(ht1, ht2, ht3) == ht2:
        #print(f'Length of h2 before pop {len(h2)}')
        h2.pop(0)
    else:
        #print(f'Length of h3 before pop {len(h3)}')
        h3.pop(0)

    return equalStacks(h1, h2, h3)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
