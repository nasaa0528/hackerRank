# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
import numpy as np 
np.set_printoptions(legacy='1.13')
n,m = list(map(int, input().split()))
narr = np.zeros((n,m))
for r in range(n): 
    narr[r] = list(map(int, input().split()))
print(np.mean(narr,axis=1))
print(np.var(narr,axis=0))
print(np.std(narr))
