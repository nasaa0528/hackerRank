"""
https://www.hackerrank.com/challenges/itertools-permutations/problem
"""
from itertools import permutations
s,k = input().split()
k = int(k)
for perm in permutations(sorted(list(s)),k):
    print("".join(perm))
