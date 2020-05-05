# https://www.hackerrank.com/challenges/np-polynomials/problem
import numpy as np 
P = np.array(list(map(float, input().split())))
x = float(input())
print(np.polyval(P, x))
