# https://www.hackerrank.com/challenges/re-start-re-end/problem
import re 
s = input() 
k = input() 
r'(?=(\d{10}))'
pattern = re.compile(r'(?=('+k+r'))')
if pattern.search(s) is None: 
    print((-1,-1)) 
else: 
    matches = pattern.finditer(s)
    for r in matches: 
        print((r.start(1), r.end(1)-1))

