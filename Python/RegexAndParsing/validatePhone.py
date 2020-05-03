# https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import re 
pattern = re.compile(r'^(7|8|9)(\d){9}$')
for case in range(int(input())): 
    if pattern.search(input()): 
        print("YES")
    else: 
        print("NO")
