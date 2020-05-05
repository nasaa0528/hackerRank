# https://www.hackerrank.com/challenges/np-min-and-max/problem
import numpy as np 
n,m = list(map(int, input().split()))
narr = np.zeros((n,m), dtype=int)
for r in range(n): 
    narr[r] = list(map(int, input().split()))
print(np.max(np.min(narr, axis=1)))
