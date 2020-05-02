#!/usr/bin/python3
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# .symmetric_difference() - returns set with all elements are in one set, but not in both
if __name__=='__main__': 
	n = int(input())
	eng_set = set(map(int, input().split()))
	b = int(input())
	fr_set = set(map(int, input().split()))
	print(len(eng_set.symmetric_difference(fr_set)))