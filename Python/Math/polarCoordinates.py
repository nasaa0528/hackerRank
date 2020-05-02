"""
https://www.hackerrank.com/challenges/polar-coordinates/problem
"""
import cmath
if __name__=="__main__":
	cnum = complex(input())
	print(abs(cnum))
	print(cmath.phase(cnum))
