# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
import re 
pattern = re.compile(r'[aeiouAEIOU]{2,}')
s = input()
if pattern.search(s) is None: 
    print(-1)
else:
    mo_iterator = pattern.finditer(s)
    for mo in mo_iterator:
        if s[mo.start()-1] in 'BCDFGHJKLMNPQRSTVXZbcdfghjklmnpqrstvxz' and s[mo.end()] in 'BCDFGHJKLMNPQRSTVXZbcdfghjklmnpqrstvxz': 
            print(mo.group())
        
