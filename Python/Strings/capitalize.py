#!/bin/python3
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# https://www.hackerrank.com/challenges/capitalize/problem
import math
import os
import random
import re
import sys

def solve(s):
    for i in range(len(s)): 
        if i == 0 and s[i].isalpha(): 
            s = s[i].upper() + s[i+1:]
        elif i > 0 and s[i-1].isspace() and s[i].isalpha(): 
            s = s[:i] + s[i].upper() + s[i+1:]
        else: 
            s = s[:i] + s[i].lower() + s[i+1:]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
