"""
.update() or |=
Update the set by adding elements from an iterable/another set.
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
TASK
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.
https://www.hackerrank.com/challenges/py-set-mutations/problem
"""
if __name__=='__main__': 
	len_A = int(input()) 
	A = set(map(int, input().split()))
	n = int(input())
	for _ in range(n): 
		operation, update_len = tuple(input().split())
		update_len = int(update_len) 
		B = set(map(int, input().split()))
		if (operation == 'intersection_update'): 
			A.intersection_update(B)
		elif (operation == 'update'): 
			A.update(B)
		elif (operation == 'symmetric_difference_update'): 
			A.symmetric_difference_update(B)
		elif (operation == 'difference_update'): 
			A.difference_update(B) 
	print(sum(A))
