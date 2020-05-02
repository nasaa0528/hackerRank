"""
https://www.hackerrank.com/challenges/itertools-combinations/problem
"""
from itertools import combinations
s,k = input().split()
k = int(k)
s = sorted(list(s))
for i in range(1,k+1): 
    result = list(combinations(s,i))
    for word in result: 
        print("".join(word))

