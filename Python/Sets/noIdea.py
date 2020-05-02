"""
There is an array of n integers. There are also 2 disjoint, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i in A, you add  to your happiness. If i in B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
https://www.hackerrank.com/challenges/no-idea/problem
"""
from collections import Counter
n,m = tuple(map(int, input().split()))
narr = list(map(int,input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
narr = dict(Counter(narr))
happies = A.intersection(narr)
sad = B.intersection(narr)

for h in happies:
	happiness += narr[h]
for s in sad: 
	happiness -= narr[s]
print(happiness)
