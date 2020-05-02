"""
https://www.hackerrank.com/challenges/python-power-mod-power/submissions/code/14056267
"""
import math
if __name__=="__main__": 
	a = int(input())
	b = int(input())
	m = int(input())
	ppow = a**b
	m_ppow = pow(a,b,m)
	print(ppow)
	print(m_ppow)
