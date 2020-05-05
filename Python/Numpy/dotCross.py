# https://www.hackerrank.com/challenges/np-dot-and-cross/problem
import numpy as np 
n = int(input())
A = np.zeros((n,n), dtype=int)
B = np.zeros((n,n), dtype=int)
for r in range(n): 
    A[r] = list(map(int, input().split()))
for r in range(n): 
    B[r] = list(map(int, input().split()))

print(np.dot(A,B))
