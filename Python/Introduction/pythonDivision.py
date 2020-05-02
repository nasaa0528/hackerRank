#!/usr/bin/python3
# https://www.hackerrank.com/challenges/python-division/problem
# Task
# Read two integers and print two lines. The first line should contain integer division, a//b. The second line should contain float division, a/b.
# You don't need to perform any rounding or formatting operations.

def division(a,b): 
	print(a//b) 
	print(a/b) 

if __name__=='__main__': 
	a = int(input()) 
	b = int(input())
	division(a,b)
