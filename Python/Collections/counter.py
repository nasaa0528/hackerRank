# https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
nums_shoes = int(input())
sz_count = dict(Counter(list(map(int,input().split()))))
profit = 0
for tr in (range(int(input()))):
    cus_size, offer = (map(int,input().split()))
    if cus_size in sz_count:
        profit += offer
        sz_count[cus_size] -=1
        if sz_count[cus_size] == 0:
            del sz_count[cus_size]
print(profit)
