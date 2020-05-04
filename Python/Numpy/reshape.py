# https://www.hackerrank.com/challenges/np-shape-reshape/problem
import numpy
arr = list(map(int, input().strip().split()))
narr = numpy.array(arr)
narr = numpy.reshape(narr,(3,3))
print(narr)


