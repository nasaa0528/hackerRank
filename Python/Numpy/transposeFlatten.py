# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
import numpy as np
n,m = list(map(int, input().split()))
narr = np.zeros((n,m),int)
for r in range(n): 
    row = list(map(int, input().split()))
    narr[r] = row 
print(np.transpose(narr), narr.flatten(), sep='\n') 
