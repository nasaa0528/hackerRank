"""
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.
https://www.hackerrank.com/challenges/py-check-subset/problem
"""
if __name__=='__main__':
	t = int(input())
	for _ in range(t): 
		len_a = int(input())
		A = set(map(int, input().split()))
		len_b = int(input())
		B = set(map(int, input().split()))
		if not A.difference(B):
			print(True)
		else:
			print(False)
