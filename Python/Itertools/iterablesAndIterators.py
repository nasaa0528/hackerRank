# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
have_A = 0
perm = list(combinations(letters,k))
for p in perm:
    if 'a' in p:
        have_A += 1
print(have_A/len(perm))
