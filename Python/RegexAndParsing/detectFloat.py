# https://www.hackerrank.com/challenges/introduction-to-regex/problem
import re 
floatRegex = re.compile(r'''^[+-]?[\d]*\.{1}[\d]+$''')
for _ in range(int(input())): 
    print(bool(floatRegex.match(input())))


