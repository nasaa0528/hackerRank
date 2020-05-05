# https://www.hackerrank.com/challenges/np-linear-algebra/problem
import numpy as np 
n = np.array(int(input()))
A = np.zeros((n,n),dtype=float)
for r in range(n): 
    A[r] = list(map(float, input().split()))
determinamt = np.linalg.det(A)
if (determinamt).is_integer():
    print("{:.1f}".format(determinamt))
else: 
    print("{:.2f}".format(determinamt))
