"""
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
"""
from itertools import combinations_with_replacement
s,k = input().split()
k = int(k)
for occurance in combinations_with_replacement(sorted(list(s)),k): 
    print("".join(occurance))
