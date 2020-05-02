#!/usr/bin/python3 
# https://www.hackerrank.com/challenges/symmetric-difference/problem
# Tutorial on Sets 
a = "5 4 3 2 1" # a = raw_input() 
lis = a.split()
newlis = list(map(int, a.split()))
print(newlis)

# Creating sets 
myset = {1,2}
print(myset)
myset = set()
print(myset)
myset = set(['a', 'b'])
print(myset)

# Modifying sets 
myset.add('c')
print(myset)
myset.add('a')
print(myset)
myset.add((5,4))
print(myset)

myset.update([1,2,3,4]) # update only works for iterable 
print(myset)
myset.update({1,7,8})
print(myset)
myset.update({1,6}, [5,13])
print(myset)

# Removing items 
# discard(value) remove(value) - then removes value
# if value is not present, remove raises error, but discard does nothing
myset.discard(10)
# myset.remove(10)
myset.remove(13)
print(myset)

# Common set operations
# union() - Values which exists in a or b - SYMMETRIC
a = {2,4,5,9}
b = {2,4,11,12}
print(a.union(b))
print(a)
print(b)

# intersection() - Values which exists in a and b - SYMMETRIC
print(a.intersection(b))
print(a)
print(b)

# difference() - exists in a but not in b 
print(a.difference(b))
print('='*50)

# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

def symmetricDifference(m,n):
	result = m.difference(n)
	result.update(n.difference(m))
	result = sorted(list(result))
	for val in result: 
		print(val)

if __name__=='__main__': 
	m = int(input())
	m_set = set(map(int,input().split()))
	# m_set = {9, 2, 4, 5}
	n = int(input())
	n_set = set(map(int, input().split()))
	# n_set = {2, 11, 4, 12}
	symmetricDifference(m_set,n_set)


