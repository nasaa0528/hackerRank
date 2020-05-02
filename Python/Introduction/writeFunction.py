#!/usr/bin/python3
# https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-introduction
# Task
# You are given the year, and you have to write a function to check if the year is leap or not.
# Note that you have to complete the function and remaining code is given as template.
def is_leap(year):
	leap = False 
	if (year % 4 == 0 and year % 100 != 0): 
		leap = True 
	elif (year % 100 == 0 and year % 400 == 0): 
		leap = True  
	return leap 

if __name__=='__main__':
	year = int(input())
	print(is_leap(year))