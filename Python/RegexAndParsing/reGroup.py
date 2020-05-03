# https://www.hackerrank.com/challenges/re-group-groups/problem
import re
regexPattern = re.compile(r'([a-zA-Z\d])\1*')
mo = list(filter(lambda x: len(x)>1, [match.group() for match in regexPattern.finditer(input())]))
if mo: 
    print(mo[0][0])
else:
    print(-1)
