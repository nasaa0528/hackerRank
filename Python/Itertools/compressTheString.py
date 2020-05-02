# https://www.hackerrank.com/challenges/compress-the-string/problem
from itertools import groupby
s = input()
result = []
for k,g in groupby(s):
    t = (len(list(g)),int(k))
    result.append(t)
for r in result: 
    print(r, end=" ")
