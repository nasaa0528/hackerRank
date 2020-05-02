# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict
if __name__=='__main__':
	A = defaultdict(list)
	n,m = map(int,input().split())
	pos = 1
	for _ in range(n):
		A[input().strip()].append(pos)
		pos += 1
	for _ in range(m):
		k = input().strip()
		if k in A:
			print(*A[k], sep=" ")
		else:
			print(-1)
