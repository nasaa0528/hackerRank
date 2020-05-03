# https://www.hackerrank.com/challenges/hex-color-code/problem
import re 
codePattern = re.compile(r'[#\.]\w+\s+{ |}')
hexPattern = re.compile(r'(#[a-fA-F\d]{6}|#[a-fA-F\d]{3})')
codeStr = []
for _ in range(int(input())): 
    codeStr.append(input().strip())
codeStr = " ".join(codeStr)
codeStr = codePattern.split(codeStr)
codeStr = list(filter(lambda x: len(x) >= 4, codeStr))
for s in codeStr: 
    matches = hexPattern.findall(s)
    if matches:
        print(*matches, sep='\n')
