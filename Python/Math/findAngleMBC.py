"""
https://www.hackerrank.com/challenges/find-angle/problem
"""
import math 
ab = int(input())
bc = int(input())
print(str(round(math.degrees(math.atan(ab/bc)))) + u"\N{DEGREE SIGN}")
