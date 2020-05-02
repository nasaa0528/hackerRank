#!/usr/bin/python3
# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# Task
# Read two integers from STDIN and print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
def arithmetic(a,b): 
	""" Gets two integer and returns example of arithmetic in python """
	print(a+b) 
	print(a-b) 
	print(a*b)

if __name__=="__main__": 
	a = int(input())
	b = int(input())
	arithmetic(a,b)

