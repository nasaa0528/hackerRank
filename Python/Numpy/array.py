# https://www.hackerrank.com/challenges/np-arrays/problem
import numpy

def arrays(arr):
    arr = list(map(float, arr))
    arr.reverse()
    return numpy.array(arr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
