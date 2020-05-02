#!/bin/python3
# https://www.hackerrank.com/challenges/py-if-else/problem
# Given an integer, n, perform the following conditional actions:
# If n is odd, print "Weird"
# If n is even and in the inclusive range of 2 to 5, print "Not Weird"
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format
# A single line containing a positive integer, n.
# Constraints
# 1 <= n <= 100
# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.

import math
import os
import random
import re
import sys
def weird_not(n):
    if (n&1 or (~(n&1) and n >= 6 and n <= 20)): 
        print("Weird")
    else: 
        print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    weird_not(n)
