#!/usr/bin/python3
# https://www.hackerrank.com/challenges/designer-door-mat/problem
# Sample output
# Size: 7 x 21 
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------


def designerDoorMat(n,m): 
	result = []
	odds = 1
	for i in range(1,int(n/2)+1):
		line = (".|." * odds).center(m,'-')
		odds += 2
		result.insert(i-1,line) 
		result.insert(-i,line) 
	result.insert(int(n/2),"WELCOME".center(m,'-'))
	for line in result: 
		print(line)

if __name__=='__main__':
	n, m = input().split()
	n = int(n)
	m = int(m) 
	designerDoorMat(n,m)

