#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax1(prices):
    stack = [-1]
    n = len(prices)
    profit = 0
    for i in range(n-1, -1, -1):
        if stack[-1]== -1:
            stack.append(prices[-1])
        elif stack[-1] >= prices[i]:
            profit += stack[-1] - prices[i]
        else:
            stack[-1] = prices[i]
    return profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
