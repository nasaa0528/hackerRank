#!/usr/bin/python3
# https://www.hackerrank.com/challenges/string-validators/problem
if __name__=='__main__': 
	s = input()
	alphaNum = False 
	alpha = False 
	digit = False 
	lower = False 
	upper = False 
	for i in range(len(s)): 
		if s[i].isalnum():
			alphaNum = True 
			if s[i].isalpha():
				alpha = True 
				if s[i].islower(): 
					lower = True
				elif s[i].isupper():
					upper = True 
			elif s[i].isdigit(): 
				digit = True 
		if alphaNum and alpha and digit and lower and upper: 
			break
	print(alphaNum)
	print(alpha)
	print(digit)
	print(lower)
	print(upper)

