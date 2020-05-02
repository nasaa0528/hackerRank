# https://www.hackerrank.com/challenges/maximize-it/submissions/code/156409076
from itertools import product
def f(x):
    return x**2
k,m = map(int,input().split())
A = []
for _ in range(k): 
    A.append(list(map(int,input().split()[1:])))
A = list(product(*A))
maxes = [(sum(list(map(f,item))))%m for item in A]
print(max(maxes))

