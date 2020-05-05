# https://www.hackerrank.com/challenges/np-concatenate/problem
import numpy as np 
n,m,p = list(map(int, input().split()))
np_arr = np.zeros((n,p),int)
mp_arr = np.zeros((m,p),int)
for r in range(n): 
    np_arr[r] = list(map(int, input().split()))

for r in range(m): 
    mp_arr[r] = list(map(int, input().split()))
print(np.concatenate((np_arr, mp_arr)))
