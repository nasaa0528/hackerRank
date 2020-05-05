# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
import numpy as np 
shape = tuple(map(int, input().split()))
zeros = np.zeros(shape, dtype=np.int)
ones = np.ones(shape, dtype=np.int)
print(zeros, ones, sep='\n')
