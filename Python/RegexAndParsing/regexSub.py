# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
import re 
andPattern = re.compile(r'[\s]&&(?=[\s])')
orPattern = re.compile(r'[\s]\|\|(?=[\s])')

for _ in range(int(input())): 
    line = input()
    line = andPattern.sub(" and", line)
    line = orPattern.sub(" or", line)
    print(line)


