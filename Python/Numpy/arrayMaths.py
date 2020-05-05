# https://www.hackerrank.com/challenges/np-array-mathematics/problem
import numpy as np 
n,m = list(map(int, input().split()))
A = np.zeros((n,m), dtype=np.int)
B = np.zeros((n,m), dtype=np.int)
for r in range(n):
    A[r] = list(map(int, input().split()))
for r in range(n):
    B[r] = list(map(int, input().split()))
print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(A // B)
print(np.mod(A,B))
print(np.power(A,B))
