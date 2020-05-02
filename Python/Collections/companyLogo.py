#!/bin/python3
# https://www.hackerrank.com/challenges/most-commons/problem
from collections import Counter 
if __name__ == '__main__':
    s = input()
    s = list(Counter(s).most_common())
    s = sorted(sorted(s,key=lambda element: element[0]),key=lambda element:element[1],reverse=True)
    for it in s[:3]: 
        print(*it, sep=' ')
