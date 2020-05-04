# https://www.hackerrank.com/challenges/matrix-script/problem
#!/bin/python3
import math
import os
import random
import re
import sys
subPattern = re.compile(r'((?=(\[a-zA-Z\d]))(!@#$%&\s)(?=(\[a-zA-Z\d])))')
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)
matrix = list(zip(*matrix))
for i in range(len(matrix)): 
    matrix[i] = "".join(matrix[i])
matrix = "".join(matrix)
matrix = re.sub(r"([a-zA-Z\d])([!@#$%&\s]+)([a-zA-Z\d])", r"\1 \3",matrix)
print(matrix)
