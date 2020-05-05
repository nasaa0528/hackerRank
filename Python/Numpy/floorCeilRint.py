# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
import numpy as np 
np.set_printoptions(legacy='1.13')
narr = np.array(list(map(float, input().split())), dtype=float)
print(np.floor(narr))
print(np.ceil(narr))
print(np.rint(narr))

