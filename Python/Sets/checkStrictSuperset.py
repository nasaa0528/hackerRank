"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of theN  sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
https://www.hackerrank.com/challenges/py-check-strict-superset/problem
"""
if __name__=='__main__': 
	A = set(map(int, input().split()))
	n = int(input())
	superSet = True
	for _ in range(n): 
		B = set(map(int, input().split()))
		if B.difference(A) or (len(A) <= len(B)):
			superSet = False
			break 
	print(superSet)
