"""
https://www.hackerrank.com/challenges/itertools-product/problem
"""
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
AB = list(product(A,B))
for item in AB: 
    print(item, end=' ')
