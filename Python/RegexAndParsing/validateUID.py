# https://www.hackerrank.com/challenges/validating-uid/problem
import re 
from collections import Counter
uidPattern = re.compile(r'^(?=([a-zA-Z\d]*\d){3})(?=([a-zA-Z\d]*[A-Z]){2})[a-zA-Z\d]*$')
def repeated(s):
    rep = Counter(s)
    if (len(list(rep)) == 10): 
        return True
    else: 
        return False

for _ in range(int(input())): 
    s = input()
    rep = Counter(s)
    if (repeated(s) and uidPattern.match(s)): 
        print("Valid")
    else: 
        print("Invalid")
